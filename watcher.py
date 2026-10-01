#!/usr/bin/env python3
"""
HF Model Watcher
----------------
Watches the Hugging Face Hub for new models in a few categories (vision,
speech, Indonesian LLMs by default), keeps a growing CSV catalog per category,
and writes a daily report of what was added.

  catalog/<category>.csv           every model ever caught, with first-seen date
  reports/YYYY/MM/YYYY-MM-DD.md    models added on that day
  README.md                        recent additions per category + totals

A model is added once (first sighting). Its likes/downloads are refreshed while
it keeps showing up in the feed. If no new model was found, nothing is written
and the workflow makes no commit.
"""
from __future__ import annotations

import csv
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from huggingface_hub import HfApi

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
CATALOG_DIR = ROOT / "catalog"
REPORT_DIR = ROOT / "reports"
README = ROOT / "README.md"
README_START = "<!-- WATCHER_START -->"
README_END = "<!-- WATCHER_END -->"

FIELDS = ["model_id", "author", "task", "library", "params_b", "license", "base_model",
          "languages", "created_at", "first_seen", "likes", "downloads", "url"]
EXPAND = ["author", "createdAt", "likes", "downloads", "pipeline_tag", "tags",
          "library_name", "trendingScore", "safetensors"]
EXCLUDE = re.compile("|".join(CONFIG.get("exclude_name_patterns", [])) or r"$^", re.I)
# ISO 639-1 codes are 2 letters; a few 3-letter ones matter for the region.
LANG_TAG = re.compile(r"^(?:[a-z]{2}|jv|su|ban|min|ace|bug|mad|bjn)$")


# --------------------------------------------------------------------------- #
# Hub access
# --------------------------------------------------------------------------- #
def list_models(api: HfApi, retries: int = 3, **kwargs) -> list:
    for attempt in range(1, retries + 1):
        try:
            return list(api.list_models(expand=EXPAND, **kwargs))
        except Exception as e:  # noqa: BLE001 - network/rate-limit errors are retried
            if attempt == retries:
                raise
            print(f"    retry {attempt} after error: {e}", file=sys.stderr)
            time.sleep(10 * attempt)
    return []


def fetch_category(api: HfApi, cat: dict) -> list:
    """All candidate models for one category, de-duplicated."""
    seen, models = set(), []

    def add(batch):
        for m in batch:
            if m.id not in seen:
                seen.add(m.id)
                models.append(m)

    lang = cat.get("language")
    if lang:
        # Language categories: one query on the language tag, task filtered locally,
        # because many LLM repos (e.g. merged or GGUF uploads) carry no pipeline tag.
        add(list_models(api, filter=lang, sort=cat["sort"], limit=cat["fetch_limit"]))
    else:
        for tag in cat["pipeline_tags"]:
            add(list_models(api, pipeline_tag=tag, sort=cat["sort"], limit=cat["fetch_limit"]))
    return models


# --------------------------------------------------------------------------- #
# Filtering
# --------------------------------------------------------------------------- #
def task_matches(m, cat: dict) -> bool:
    if m.pipeline_tag in cat["pipeline_tags"]:
        return True
    hints = cat.get("untagged_llm_hints")
    if hints and not m.pipeline_tag:
        tags = {t.lower() for t in (m.tags or [])}
        return any(h in tags for h in hints)
    return False


def keep(m, cat: dict, now: datetime) -> bool:
    if not m.created_at or now - m.created_at > timedelta(days=cat["max_age_days"]):
        return False
    if EXCLUDE.search(m.id.split("/")[-1]):
        return False
    if not task_matches(m, cat):
        return False
    likes, downloads = m.likes or 0, m.downloads or 0
    if cat["min_likes"] or cat["min_downloads"]:
        return likes >= cat["min_likes"] or downloads >= cat["min_downloads"]
    return True


def tag_value(tags: list[str], prefix: str) -> str:
    for t in tags:
        if t.startswith(prefix):
            return t[len(prefix):]
    return ""


def to_row(m, today: str) -> dict:
    tags = m.tags or []
    params = ""
    st = getattr(m, "safetensors", None)
    if st is not None and getattr(st, "total", None):
        params = f"{st.total / 1e9:.2f}"
    task = m.pipeline_tag or ("gguf" if "gguf" in tags else "")
    return {
        "model_id": m.id,
        "author": m.author or m.id.split("/")[0],
        "task": task,
        "library": m.library_name or "",
        "params_b": params,
        "license": tag_value(tags, "license:"),
        "base_model": tag_value(tags, "base_model:").split(":", 1)[-1],
        "languages": " ".join(t for t in tags if LANG_TAG.match(t)),
        "created_at": m.created_at.strftime("%Y-%m-%d"),
        "first_seen": today,
        "likes": m.likes or 0,
        "downloads": m.downloads or 0,
        "url": f"https://huggingface.co/{m.id}",
    }


# --------------------------------------------------------------------------- #
# Catalog
# --------------------------------------------------------------------------- #
def load_catalog(key: str) -> dict[str, dict]:
    path = CATALOG_DIR / f"{key}.csv"
    if not path.exists():
        return {}
    with path.open(encoding="utf-8", newline="") as f:
        return {r["model_id"]: r for r in csv.DictReader(f)}


def save_catalog(key: str, rows: dict[str, dict]) -> None:
    path = CATALOG_DIR / f"{key}.csv"
    ordered = sorted(rows.values(), key=lambda r: (r["first_seen"], r["created_at"], r["model_id"]),
                     reverse=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(ordered)


# --------------------------------------------------------------------------- #
# Reports
# --------------------------------------------------------------------------- #
def fmt_num(n) -> str:
    n = int(n or 0)
    return f"{n / 1e6:.1f}M" if n >= 1e6 else f"{n / 1e3:.1f}k" if n >= 1e3 else str(n)


def model_table(rows: list[dict]) -> list[str]:
    lines = ["| Model | Task | Size | License | ❤️ | ⬇️ | Created |",
             "|-------|------|-----:|---------|---:|---:|---------|"]
    for r in rows:
        size = f"{float(r['params_b']):g}B" if r["params_b"] else "–"
        lines.append(f"| [{r['model_id']}]({r['url']}) | {r['task'] or '–'} | {size} "
                     f"| {r['license'] or '–'} | {fmt_num(r['likes'])} | {fmt_num(r['downloads'])} "
                     f"| {r['created_at']} |")
    return lines


def write_report(today: str, catalogs: dict[str, dict[str, dict]]) -> Path:
    # built from the catalog, so a second run on the same day keeps the first run's models
    added = {k: [r for r in rows.values() if r["first_seen"] == today] for k, rows in catalogs.items()}
    y, m, _ = today.split("-")
    path = REPORT_DIR / y / m / f"{today}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    total = sum(len(v) for v in added.values())
    lines = [f"# New models on Hugging Face — {today}", "",
             f"{total} model(s) added to the catalog today.", ""]
    for key, rows in added.items():
        if not rows:
            continue
        cat = CONFIG["categories"][key]
        rows = sorted(rows, key=lambda r: (int(r["likes"]), int(r["downloads"])), reverse=True)
        lines += [f"## {cat['label']} ({len(rows)})", "", *model_table(rows), ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def update_readme(today: str, catalogs: dict[str, dict[str, dict]], report: Path) -> None:
    if not README.exists():
        return
    text = README.read_text(encoding="utf-8")
    if README_START not in text or README_END not in text:
        return
    since = (datetime.fromisoformat(today) - timedelta(days=CONFIG["readme_recent_days"] - 1)).strftime("%Y-%m-%d")
    totals = " · ".join(f"{CONFIG['categories'][k]['label']}: {len(v)}" for k, v in catalogs.items())
    block = [README_START,
             f"_Last updated {today} · catalog size: {totals} · "
             f"[today's report]({report.relative_to(ROOT).as_posix()})_", ""]
    for key, rows in catalogs.items():
        cat = CONFIG["categories"][key]
        recent = [r for r in rows.values() if r["first_seen"] >= since]
        recent.sort(key=lambda r: (int(r["likes"]), int(r["downloads"])), reverse=True)
        block += [f"### {cat['label']}", "", cat["description"], ""]
        if recent:
            block += [f"Most-liked of the {len(recent)} added in the last {CONFIG['readme_recent_days']} days:", "",
                      *model_table(recent[: CONFIG["readme_per_category"]])]
        else:
            block += [f"_No new models in the last {CONFIG['readme_recent_days']} days._"]
        block += ["", f"[Full catalog →](catalog/{key}.csv)", ""]
    block.append(README_END)
    pattern = re.compile(re.escape(README_START) + r".*?" + re.escape(README_END), re.S)
    README.write_text(pattern.sub(lambda _: "\n".join(block), text), encoding="utf-8")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main(api: HfApi | None = None) -> int:
    api = api or HfApi(token=os.getenv("HF_TOKEN") or None)
    CATALOG_DIR.mkdir(exist_ok=True)
    now = datetime.now(timezone.utc)
    today = datetime.now(ZoneInfo(CONFIG.get("timezone", "UTC"))).strftime("%Y-%m-%d")

    catalogs: dict[str, dict[str, dict]] = {}
    added: dict[str, list[dict]] = {}
    for key, cat in CONFIG["categories"].items():
        print(f"[{cat['label']}]")
        catalog = load_catalog(key)
        catalogs[key] = catalog
        try:
            candidates = fetch_category(api, cat)
        except Exception as e:  # noqa: BLE001 - one failing category must not stop the rest
            print(f"  ! skipped: {e}", file=sys.stderr)
            added[key] = []
            continue
        kept = [m for m in candidates if keep(m, cat, now)]
        new_rows = []
        for m in kept:
            row = to_row(m, today)
            if m.id in catalog:  # refresh popularity, keep the original first_seen
                catalog[m.id]["likes"], catalog[m.id]["downloads"] = row["likes"], row["downloads"]
            else:
                catalog[m.id] = row
                new_rows.append(row)
        added[key] = new_rows
        print(f"  {len(candidates)} fetched, {len(kept)} passed filters, {len(new_rows)} new")

    if not any(added.values()):
        print("No new models. Nothing to commit.")
        return 0

    for key, catalog in catalogs.items():
        save_catalog(key, catalog)
    report = write_report(today, catalogs)
    update_readme(today, catalogs, report)
    print(f"Wrote {report.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
