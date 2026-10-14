# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-10-14 · catalog size: Vision: 180 · Speech: 124 · LLM Indonesia: 195 · [today's report](reports/2026/10/2026-10-14.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 53 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [openbmb/MiniCPM-V-4.7-35B-A3B](https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B) | image-text-to-text | 35.21B | apache-2.0 | 491 | 630 | 2026-10-07 |
| [LiquidAI/d1-3B](https://huggingface.co/LiquidAI/d1-3B) | image-text-to-text | 3.12B | other | 383 | 13.2k | 2026-10-05 |
| [nerkyor/Qwen3.8-27B-Coder390-EfficientThink-Opus5.5-GPT6Astra-Grok4.7-DSV4Pro-K3-SFT-RLOO-MTP-DFlash2](https://huggingface.co/nerkyor/Qwen3.8-27B-Coder390-EfficientThink-Opus5.5-GPT6Astra-Grok4.7-DSV4Pro-K3-SFT-RLOO-MTP-DFlash2) | image-text-to-text | – | apache-2.0 | 312 | 83.9k | 2026-10-04 |
| [openbmb/MiniCPM-V-4.7-1B](https://huggingface.co/openbmb/MiniCPM-V-4.7-1B) | image-text-to-text | 1.55B | apache-2.0 | 294 | 263 | 2026-10-06 |
| [autotrust/GLM5.3-Flash-E192-DGX-Spark](https://huggingface.co/autotrust/GLM5.3-Flash-E192-DGX-Spark) | image-text-to-text | 110.71B | mit | 176 | 4.5k | 2026-10-09 |
| [DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 121 | 14.8k | 2026-09-29 |
| [LiquidAI/d1-omni-600M](https://huggingface.co/LiquidAI/d1-omni-600M) | image-text-to-text | 0.59B | other | 120 | 11.5k | 2026-10-05 |
| [Cloudflare/clef-omni](https://huggingface.co/Cloudflare/clef-omni) | image-text-to-text | 35.26B | apache-2.0 | 117 | 1.2k | 2026-10-09 |
| [autotrust/GLM5.3-Flash-E256-DGX-Spark](https://huggingface.co/autotrust/GLM5.3-Flash-E256-DGX-Spark) | image-text-to-text | 144.54B | mit | 114 | 2.3k | 2026-10-09 |
| [openbmb/MiniCPM-V-4.7-35B-A3B-gguf](https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B-gguf) | image-text-to-text | – | apache-2.0 | 96 | 10.1k | 2026-10-06 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 33 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [fishaudio/drama-3](https://huggingface.co/fishaudio/drama-3) | text-to-speech | 35.9B | other | 159 | 23 | 2026-10-01 |
| [neuphonic/neudecide](https://huggingface.co/neuphonic/neudecide) | audio-classification | – | apache-2.0 | 74 | 554 | 2026-10-06 |
| [sahilmahendrakar/Paradee-8M-v1.0](https://huggingface.co/sahilmahendrakar/Paradee-8M-v1.0) | text-to-speech | – | apache-2.0 | 51 | 1.9k | 2026-09-25 |
| [cloud0day3/antalia-mini](https://huggingface.co/cloud0day3/antalia-mini) | text-to-speech | – | apache-2.0 | 39 | 1.6k | 2026-10-08 |
| [mistralai/Voxtral-Mini-4B-Realtime-Arabic](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-Arabic) | automatic-speech-recognition | 4.43B | – | 31 | 574 | 2026-10-08 |
| [qnguyen3/QUAN-Transcribe-1.0](https://huggingface.co/qnguyen3/QUAN-Transcribe-1.0) | automatic-speech-recognition | 0.1B | gemma | 12 | 0 | 2026-10-14 |
| [erkamk/qwen3-tts-tiny-tr](https://huggingface.co/erkamk/qwen3-tts-tiny-tr) | text-to-speech | 0.2B | apache-2.0 | 11 | 287 | 2026-10-02 |
| [TeamUNIVA/qwen3_asr_1.7b_ko](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko) | automatic-speech-recognition | 2.35B | apache-2.0 | 11 | 26 | 2026-10-12 |
| [edwixx/rapido-tts](https://huggingface.co/edwixx/rapido-tts) | text-to-speech | – | apache-2.0 | 9 | 0 | 2026-10-07 |
| [ozcancelik/ema-lightning-onnx](https://huggingface.co/ozcancelik/ema-lightning-onnx) | text-to-speech | – | apache-2.0 | 7 | 0 | 2026-10-07 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 76 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [LiquidAI/d1-3B](https://huggingface.co/LiquidAI/d1-3B) | image-text-to-text | 3.12B | other | 383 | 13.2k | 2026-10-05 |
| [LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) | text-generation | 23.97B | other | 203 | 2.6k | 2026-10-12 |
| [DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 121 | 14.8k | 2026-09-29 |
| [interfaze-ai/interfaze-1-lite](https://huggingface.co/interfaze-ai/interfaze-1-lite) | image-text-to-text | – | other | 63 | 215 | 2026-10-03 |
| [LiquidAI/d1-3B-GGUF](https://huggingface.co/LiquidAI/d1-3B-GGUF) | image-text-to-text | – | other | 53 | 19.1k | 2026-10-06 |
| [LiquidAI/LFM2.5-24B-A2B-Base](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-Base) | text-generation | 23.97B | other | 28 | 7 | 2026-10-09 |
| [unsloth/LFM2.5-24B-A2B-GGUF](https://huggingface.co/unsloth/LFM2.5-24B-A2B-GGUF) | text-generation | – | other | 25 | 0 | 2026-10-13 |
| [LiquidAI/d1-3B-w8a8](https://huggingface.co/LiquidAI/d1-3B-w8a8) | image-text-to-text | 3.13B | other | 7 | 221 | 2026-10-07 |
| [DavidAU/LFM2.5-24B-A2B-Turbo-Brilliance-50X-NEO-MAX-Imatrix-GGUF](https://huggingface.co/DavidAU/LFM2.5-24B-A2B-Turbo-Brilliance-50X-NEO-MAX-Imatrix-GGUF) | text-generation | – | other | 7 | 0 | 2026-10-13 |
| [unsloth/LFM2.5-24B-A2B](https://huggingface.co/unsloth/LFM2.5-24B-A2B) | text-generation | 23.97B | other | 4 | 2 | 2026-10-13 |

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
