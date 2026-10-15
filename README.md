# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-10-15 · catalog size: Vision: 186 · Speech: 134 · LLM Indonesia: 209 · [today's report](reports/2026/10/2026-10-15.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 50 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [openbmb/MiniCPM-V-4.7-35B-A3B](https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B) | image-text-to-text | 35.21B | apache-2.0 | 675 | 4.2k | 2026-10-07 |
| [openbmb/MiniCPM-V-4.7-1B](https://huggingface.co/openbmb/MiniCPM-V-4.7-1B) | image-text-to-text | 1.55B | apache-2.0 | 338 | 2.5k | 2026-10-06 |
| [autotrust/GLM5.3-Flash-E192-DGX-Spark](https://huggingface.co/autotrust/GLM5.3-Flash-E192-DGX-Spark) | image-text-to-text | 110.71B | mit | 177 | 6.0k | 2026-10-09 |
| [DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 134 | 47.8k | 2026-09-29 |
| [openbmb/MiniCPM-V-4.7-35B-A3B-gguf](https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B-gguf) | image-text-to-text | – | apache-2.0 | 124 | 47.0k | 2026-10-06 |
| [Cloudflare/clef-omni](https://huggingface.co/Cloudflare/clef-omni) | image-text-to-text | 35.26B | apache-2.0 | 118 | 1.9k | 2026-10-09 |
| [autotrust/GLM5.3-Flash-E256-DGX-Spark](https://huggingface.co/autotrust/GLM5.3-Flash-E256-DGX-Spark) | image-text-to-text | 144.54B | mit | 115 | 3.0k | 2026-10-09 |
| [tencent/Youtu-Parsing-Omni](https://huggingface.co/tencent/Youtu-Parsing-Omni) | image-text-to-text | 5.33B | other | 97 | 1.2k | 2026-10-09 |
| [lightonai/LightOnOCR-3-4B](https://huggingface.co/lightonai/LightOnOCR-3-4B) | image-text-to-text | 4.54B | apache-2.0 | 91 | 7.9k | 2026-10-06 |
| [interfaze-ai/interfaze-1-lite](https://huggingface.co/interfaze-ai/interfaze-1-lite) | image-text-to-text | – | other | 67 | 245 | 2026-10-03 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 36 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [fishaudio/drama-3](https://huggingface.co/fishaudio/drama-3) | text-to-speech | 35.9B | other | 342 | 839 | 2026-10-01 |
| [neuphonic/neudecide](https://huggingface.co/neuphonic/neudecide) | audio-classification | – | apache-2.0 | 76 | 571 | 2026-10-06 |
| [cloud0day3/antalia-mini](https://huggingface.co/cloud0day3/antalia-mini) | text-to-speech | – | apache-2.0 | 42 | 1.8k | 2026-10-08 |
| [qnguyen3/QUAN-Transcribe-1.0](https://huggingface.co/qnguyen3/QUAN-Transcribe-1.0) | automatic-speech-recognition | 0.1B | gemma | 42 | 33 | 2026-10-14 |
| [mistralai/Voxtral-Mini-4B-Realtime-Arabic](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-Arabic) | automatic-speech-recognition | 4.43B | – | 33 | 684 | 2026-10-08 |
| [KaanAydinli/Duyu-small](https://huggingface.co/KaanAydinli/Duyu-small) | automatic-speech-recognition | – | apache-2.0 | 18 | 16 | 2026-10-11 |
| [TeamUNIVA/qwen3_asr_1.7b_ko](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko) | automatic-speech-recognition | 2.35B | apache-2.0 | 11 | 69 | 2026-10-12 |
| [akhaliq/drama-3-int4](https://huggingface.co/akhaliq/drama-3-int4) | text-to-speech | 6.86B | other | 11 | 68 | 2026-10-13 |
| [Jmica/Drama-3-GGUF](https://huggingface.co/Jmica/Drama-3-GGUF) | text-to-speech | – | other | 9 | 1.2k | 2026-10-13 |
| [edwixx/rapido-tts](https://huggingface.co/edwixx/rapido-tts) | text-to-speech | – | apache-2.0 | 9 | 0 | 2026-10-07 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 74 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) | text-generation | 23.97B | other | 323 | 4.1k | 2026-10-12 |
| [DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 121 | 14.8k | 2026-09-29 |
| [interfaze-ai/interfaze-1-lite](https://huggingface.co/interfaze-ai/interfaze-1-lite) | image-text-to-text | – | other | 67 | 245 | 2026-10-03 |
| [unsloth/LFM2.5-24B-A2B-GGUF](https://huggingface.co/unsloth/LFM2.5-24B-A2B-GGUF) | text-generation | – | other | 44 | 3.2k | 2026-10-13 |
| [LiquidAI/LFM2.5-24B-A2B-Base](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-Base) | text-generation | 23.97B | other | 32 | 73 | 2026-10-09 |
| [DavidAU/LFM2.5-24B-A2B-Turbo-Brilliance-50X-NEO-MAX-Imatrix-GGUF](https://huggingface.co/DavidAU/LFM2.5-24B-A2B-Turbo-Brilliance-50X-NEO-MAX-Imatrix-GGUF) | text-generation | – | other | 12 | 0 | 2026-10-13 |
| [DavidAU/Qwen3.8-Flash-Next-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-Flash-Next-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 10 | 0 | 2026-10-13 |
| [unsloth/LFM2.5-24B-A2B](https://huggingface.co/unsloth/LFM2.5-24B-A2B) | text-generation | 23.97B | other | 4 | 351 | 2026-10-13 |
| [IsValorum/LFM2.5-24B-A2B-APEX-I-MiniPlus-V2.1-GGUF](https://huggingface.co/IsValorum/LFM2.5-24B-A2B-APEX-I-MiniPlus-V2.1-GGUF) | text-generation | – | other | 3 | 170 | 2026-10-13 |
| [OceanLabs/Coral-2-3B-fast](https://huggingface.co/OceanLabs/Coral-2-3B-fast) | image-text-to-text | 3.12B | other | 3 | 68 | 2026-10-10 |

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
