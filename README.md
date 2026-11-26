# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-26 · catalog size: Vision: 534 · Speech: 520 · LLM Indonesia: 840 · [today's report](reports/2026/11/2026-11-26.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 76 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [thinkingmachines/Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini) | image-text-to-text | 26.39B | apache-2.0 | 6.1k | 96.5k | 2026-11-17 |
| [unsloth/Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF) | image-text-to-text | – | apache-2.0 | 1.4k | 2.4M | 2026-11-20 |
| [apple/DepthPro2](https://huggingface.co/apple/DepthPro2) | depth-estimation | – | other | 1.3k | 0 | 2026-11-03 |
| [AtomicChat/Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF) | image-text-to-text | – | apache-2.0 | 865 | 762.5k | 2026-11-20 |
| [tencent/Hy4](https://huggingface.co/tencent/Hy4) | image-text-to-text | 774.43B | other | 336 | 2.9k | 2026-10-29 |
| [OpenUncensored/Inkling-2-Mini-Uncensored](https://huggingface.co/OpenUncensored/Inkling-2-Mini-Uncensored) | image-text-to-text | 26.39B | apache-2.0 | 331 | 4.6k | 2026-11-20 |
| [nari-labs/Qwen3.8-27B-NariQ-GGUF](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF) | image-text-to-text | – | apache-2.0 | 170 | 14.3k | 2026-11-20 |
| [strata-engine/Inkling-2-Mini-Strata](https://huggingface.co/strata-engine/Inkling-2-Mini-Strata) | image-text-to-text | – | apache-2.0 | 167 | 3.0k | 2026-11-21 |
| [AtomicChat/Inkling-2-Mini-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-GGUF) | image-text-to-text | – | apache-2.0 | 161 | 177.0k | 2026-11-20 |
| [thinkingmachines/TML-d24-varloop-research](https://huggingface.co/thinkingmachines/TML-d24-varloop-research) | image-text-to-text | 26.39B | apache-2.0 | 155 | 3.4k | 2026-11-18 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 71 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [adventists-ai/Sophon-Realtime-v1](https://huggingface.co/adventists-ai/Sophon-Realtime-v1) | audio-to-audio | – | apache-2.0 | 263 | 61 | 2026-11-07 |
| [StudioYebisu-ship-it/Drama-3-Japanese-speech-cpp-gguf](https://huggingface.co/StudioYebisu-ship-it/Drama-3-Japanese-speech-cpp-gguf) | text-to-speech | – | other | 93 | 35.9k | 2026-11-23 |
| [mehdi-hf/tiny-ava](https://huggingface.co/mehdi-hf/tiny-ava) | text-to-speech | – | cc-by-4.0 | 23 | 133 | 2026-11-23 |
| [adventists-ai/Sophon-Realtime-4B-Flash](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-Flash) | audio-to-audio | – | apache-2.0 | 22 | 984 | 2026-11-16 |
| [oddadmix/tiny-voca-arabic](https://huggingface.co/oddadmix/tiny-voca-arabic) | text-to-speech | – | apache-2.0 | 21 | 182 | 2026-11-21 |
| [oruk/oruk-fourier-2b](https://huggingface.co/oruk/oruk-fourier-2b) | automatic-speech-recognition | 2.04B | cc-by-nc-4.0 | 19 | 2.3k | 2026-11-20 |
| [KaleComputer/kale-tts-1-nano](https://huggingface.co/KaleComputer/kale-tts-1-nano) | text-to-speech | – | apache-2.0 | 19 | 456 | 2026-11-16 |
| [adventists-ai/Sophon-Realtime-32B-Tag](https://huggingface.co/adventists-ai/Sophon-Realtime-32B-Tag) | audio-to-audio | – | apache-2.0 | 16 | 1.3k | 2026-10-29 |
| [Metric-AI/OhanASR-v0.1](https://huggingface.co/Metric-AI/OhanASR-v0.1) | automatic-speech-recognition | – | cc-by-nc-4.0 | 16 | 0 | 2026-11-08 |
| [Ekam/Libra-TTS](https://huggingface.co/Ekam/Libra-TTS) | text-to-speech | 0.31B | apache-2.0 | 15 | 360 | 2026-11-19 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 98 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [huihui-ai/Huihui-Mistral-Large-4-1T-A52B-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-Mistral-Large-4-1T-A52B-abliterated-GGUF) | gguf | – | mit | 7 | 33 | 2026-11-25 |
| [PeterPetir/Qwen3.5-9B-Shrunk-OutQ6K-GGUF](https://huggingface.co/PeterPetir/Qwen3.5-9B-Shrunk-OutQ6K-GGUF) | text-generation | – | apache-2.0 | 5 | 818 | 2026-11-22 |
| [prithivMLmods/Domyn-Edge-Teacher-Math-GGUF](https://huggingface.co/prithivMLmods/Domyn-Edge-Teacher-Math-GGUF) | text-generation | – | apache-2.0 | 3 | 753 | 2026-11-20 |
| [prithivMLmods/Domyn-Edge-Teacher-Code-GGUF](https://huggingface.co/prithivMLmods/Domyn-Edge-Teacher-Code-GGUF) | text-generation | – | apache-2.0 | 3 | 741 | 2026-11-20 |
| [Rosa-AI/Hips1.0-0.8B](https://huggingface.co/Rosa-AI/Hips1.0-0.8B) | text-generation | 0.75B | other | 3 | 105 | 2026-11-20 |
| [AdelKazzaz/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/AdelKazzaz/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 1 | 24.5k | 2026-11-20 |
| [prithivMLmods/Domyn-Edge-SFT-GGUF](https://huggingface.co/prithivMLmods/Domyn-Edge-SFT-GGUF) | text-generation | – | apache-2.0 | 1 | 1.5k | 2026-11-20 |
| [KiyoEditz/Elaina-gemma-4-31B-v0.1-GGUF](https://huggingface.co/KiyoEditz/Elaina-gemma-4-31B-v0.1-GGUF) | text-generation | – | other | 1 | 948 | 2026-11-19 |
| [prithivMLmods/Domyn-Edge-Teacher-IF-GGUF](https://huggingface.co/prithivMLmods/Domyn-Edge-Teacher-IF-GGUF) | text-generation | – | apache-2.0 | 1 | 828 | 2026-11-20 |
| [mradermacher/Kanata-S1-3B-i1-GGUF](https://huggingface.co/mradermacher/Kanata-S1-3B-i1-GGUF) | gguf | – | apache-2.0 | 1 | 755 | 2026-11-23 |

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
