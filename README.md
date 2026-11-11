# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-11 · catalog size: Vision: 406 · Speech: 356 · LLM Indonesia: 629 · [today's report](reports/2026/11/2026-11-11.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 43 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [autotrust/Qwen3.8-Flash-Next-E384-FP4-V2](https://huggingface.co/autotrust/Qwen3.8-Flash-Next-E384-FP4-V2) | image-text-to-text | 80.08B | other | 2.4k | 49.2k | 2026-10-26 |
| [moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) | image-text-to-text | 2780.11B | other | 1.9k | 30.7k | 2026-11-02 |
| [Cactus-Compute/mirage](https://huggingface.co/Cactus-Compute/mirage) | image-text-to-text | – | apache-2.0 | 136 | 12.8k | 2026-11-05 |
| [fastino/GLiDE-27B](https://huggingface.co/fastino/GLiDE-27B) | image-text-to-text | 26.09B | other | 90 | 2.7k | 2026-10-19 |
| [DavidAU/Qwen3.8-27B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF) | image-text-to-text | – | apache-2.0 | 88 | 29.8k | 2026-11-04 |
| [meituan-longcat/LongCat-2.5](https://huggingface.co/meituan-longcat/LongCat-2.5) | image-text-to-text | 1779.75B | mit | 84 | 195 | 2026-11-04 |
| [maritaca-ai/S5-nano](https://huggingface.co/maritaca-ai/S5-nano) | image-text-to-text | 4.66B | apache-2.0 | 72 | 1.1k | 2026-11-02 |
| [Sparset/Thinklite-27B](https://huggingface.co/Sparset/Thinklite-27B) | image-text-to-text | 27.78B | apache-2.0 | 48 | 477 | 2026-10-30 |
| [bartowski/NousResearch_Arete-27B-GGUF](https://huggingface.co/bartowski/NousResearch_Arete-27B-GGUF) | image-text-to-text | – | apache-2.0 | 39 | 53.9k | 2026-11-06 |
| [higa2515/Qwen3.8-27B-QSA-GGUF](https://huggingface.co/higa2515/Qwen3.8-27B-QSA-GGUF) | image-text-to-text | – | apache-2.0 | 27 | 11.2k | 2026-11-04 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 52 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [ConwayResearch/Underdog-Woof](https://huggingface.co/ConwayResearch/Underdog-Woof) | text-to-speech | – | other | 152 | 10 | 2026-11-05 |
| [Zyphra/ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini) | text-to-speech | – | apache-2.0 | 92 | 856 | 2026-11-09 |
| [Oomni/mithi-v1-flash](https://huggingface.co/Oomni/mithi-v1-flash) | text-to-speech | – | apache-2.0 | 62 | 243 | 2026-11-07 |
| [Prahaladha/hima-asr](https://huggingface.co/Prahaladha/hima-asr) | automatic-speech-recognition | 0.46B | other | 21 | 1.5k | 2026-10-12 |
| [klein-ml/Klein-TTS-X1.5-Pro](https://huggingface.co/klein-ml/Klein-TTS-X1.5-Pro) | text-to-speech | 0.01B | apache-2.0 | 10 | 200 | 2026-11-03 |
| [goldhub/YuE2-RS-Finetunes](https://huggingface.co/goldhub/YuE2-RS-Finetunes) | text-to-audio | – | cc-by-nc-sa-4.0 | 9 | 12.1k | 2026-10-22 |
| [t8star/Drama-3-Comfy](https://huggingface.co/t8star/Drama-3-Comfy) | text-to-speech | – | other | 7 | 263 | 2026-10-15 |
| [gertelrina/aadd](https://huggingface.co/gertelrina/aadd) | audio-classification | – | mit | 7 | 45 | 2026-11-05 |
| [anwar-dev/Bayan-Arabic-TTS-v1.0](https://huggingface.co/anwar-dev/Bayan-Arabic-TTS-v1.0) | text-to-speech | – | other | 6 | 349 | 2026-10-21 |
| [sahilmahendrakar/Paradee-8M-v1.3](https://huggingface.co/sahilmahendrakar/Paradee-8M-v1.3) | text-to-speech | – | apache-2.0 | 6 | 290 | 2026-11-06 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 141 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [DavidAU/Qwen3.8-27B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF) | image-text-to-text | – | apache-2.0 | 88 | 29.8k | 2026-11-04 |
| [DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF) | image-text-to-text | – | apache-2.0 | 24 | 173 | 2026-11-10 |
| [DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Build2](https://huggingface.co/DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Build2) | image-text-to-text | 39.96B | apache-2.0 | 18 | 117 | 2026-11-03 |
| [orcarouter/LFM3-1.7B-abliterated-GGUF](https://huggingface.co/orcarouter/LFM3-1.7B-abliterated-GGUF) | text-generation | – | other | 10 | 328 | 2026-11-05 |
| [speakleash/Bielik-11B-v3.1-Instruct-GGUF](https://huggingface.co/speakleash/Bielik-11B-v3.1-Instruct-GGUF) | gguf | – | apache-2.0 | 6 | 0 | 2026-11-10 |
| [xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge](https://huggingface.co/xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge) | text-generation | 1.73B | other | 4 | 241 | 2026-11-04 |
| [Shivansh-13929/LFM3-2.2B-Omni-Coder-Instruct](https://huggingface.co/Shivansh-13929/LFM3-2.2B-Omni-Coder-Instruct) | text-generation | 2.17B | other | 3 | 148 | 2026-11-04 |
| [mradermacher/Mistral-Small-3.2-24B-Instruct-2506-ARA-heretic-i1-GGUF](https://huggingface.co/mradermacher/Mistral-Small-3.2-24B-Instruct-2506-ARA-heretic-i1-GGUF) | gguf | – | apache-2.0 | 2 | 4.7k | 2026-11-06 |
| [mradermacher/Qwen3.8-27B-Uncensored-Impulsive-i1-GGUF](https://huggingface.co/mradermacher/Qwen3.8-27B-Uncensored-Impulsive-i1-GGUF) | gguf | – | apache-2.0 | 2 | 4.1k | 2026-11-05 |
| [xtools-at/LFM3-1.7B-Claude-Opus-Reasoning-Distilled-GGUF](https://huggingface.co/xtools-at/LFM3-1.7B-Claude-Opus-Reasoning-Distilled-GGUF) | text-generation | – | other | 2 | 1.1k | 2026-11-05 |

[Full catalog →](catalog/llm-indonesia.csv)

<!-- WATCHER_END -->

## How it works

```
Hugging Face Hub API ──► per-category query ──► noise filter ──► catalog/*.csv + reports/ + README
```

1. **Query.** Vision and Speech are fetched per task (e.g. `object-detection`, `automatic-speech-recognition`), sorted by trending score. LLM Indonesia is fetched by the language tag `id`, sorted by creation date.
2. **Filter.** A model is kept only if it was created in the last 30 days and its name doesn't look like a throwaway upload (`test`, `demo`, `checkpoint-500`, `tugas`, ...). Vision and Speech also require early traction (at least 3 likes or 500 downloads), because hundreds of experimental fine-tunes are uploaded every day. LLM Indonesia keeps everything, since the language is small enough to track in full.
3. **Catalog.** New models are appended with the date they were first seen. Likes and downloads are refreshed while a model stays in the feed.
4. **Report.** `reports/YYYY/MM/YYYY-MM-DD.md` lists that day's additions, sorted by likes.

If nothing new passes the filters, no file changes and no commit is made.

## Catalog format

`catalog/vision.csv`, `catalog/speech.csv`, `catalog/llm-indonesia.csv`:

| Column | Meaning |
|--------|---------|
| `model_id` | Hub repo id, e.g. `org/model-name` |
| `author` | Organization or user |
| `task` | Pipeline tag (`gguf` for GGUF uploads without one) |
| `library` | `transformers`, `gguf`, `peft`, ... |
| `params_b` | Parameter count in billions (when the repo has safetensors metadata) |
| `license` | From the repo's license tag |
| `base_model` | The model it was fine-tuned or quantized from, if declared |
| `languages` | Language tags on the repo |
| `created_at` / `first_seen` | Repo creation date / date this watcher caught it |
| `likes` / `downloads` | Popularity at last refresh |

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/arielshakaramiro/hf-model-watcher/main/catalog/llm-indonesia.csv")
df.sort_values("likes", ascending=False).head(20)
```

## Setup

1. Push this repository to GitHub.
2. Optional: add a Hugging Face read token as the secret `HF_TOKEN` (**Settings → Secrets and variables → Actions**) for higher API rate limits. It works without one.
3. **Actions → Daily Model Watch → Run workflow** to trigger the first run.

## Run locally

```bash
pip install -r requirements.txt
python watcher.py
```

## Customize

Everything lives in `config.json`:

- Add a category by adding an entry under `categories`. For a language category set `language` (e.g. `"ms"` for Malay, `"jv"` for Javanese); otherwise list `pipeline_tags`.
- `min_likes` / `min_downloads`: the traction filter (a model passes if it meets either). Set both to `0` to keep everything.
- `max_age_days`: how recent a model must be.
- `exclude_name_patterns`: regular expressions for names to skip.

## License

MIT. Model metadata comes from the public [Hugging Face Hub API](https://huggingface.co/docs/hub); each model keeps its own license.
