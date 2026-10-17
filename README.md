# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-10-17 · catalog size: Vision: 211 · Speech: 147 · LLM Indonesia: 237 · [today's report](reports/2026/10/2026-10-17.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 56 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [openbmb/MiniCPM-V-4.7-35B-A3B](https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B) | image-text-to-text | 35.21B | apache-2.0 | 859 | 17.6k | 2026-10-07 |
| [openbmb/MiniCPM-V-4.7-1B](https://huggingface.co/openbmb/MiniCPM-V-4.7-1B) | image-text-to-text | 1.55B | apache-2.0 | 369 | 8.8k | 2026-10-06 |
| [autotrust/GLM5.3-Flash-E192-DGX-Spark](https://huggingface.co/autotrust/GLM5.3-Flash-E192-DGX-Spark) | image-text-to-text | 110.71B | mit | 179 | 8.2k | 2026-10-09 |
| [nvidia/Qwen3.8-Flash-Next-FP4-Local](https://huggingface.co/nvidia/Qwen3.8-Flash-Next-FP4-Local) | image-text-to-text | 96.49B | other | 156 | 771 | 2026-10-08 |
| [openbmb/MiniCPM-V-4.7-35B-A3B-gguf](https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B-gguf) | image-text-to-text | – | apache-2.0 | 152 | 125.0k | 2026-10-06 |
| [DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 147 | 113.0k | 2026-09-29 |
| [nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4) | image-text-to-text | 65.77B | other | 120 | 2.7k | 2026-10-12 |
| [autotrust/GLM5.3-Flash-E256-DGX-Spark](https://huggingface.co/autotrust/GLM5.3-Flash-E256-DGX-Spark) | image-text-to-text | 144.54B | mit | 117 | 3.8k | 2026-10-09 |
| [nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB) | image-text-to-text | 22.37B | other | 110 | 1.1k | 2026-10-07 |
| [nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF) | image-text-to-text | – | other | 82 | 26.8k | 2026-10-07 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 42 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [fishaudio/drama-3](https://huggingface.co/fishaudio/drama-3) | text-to-speech | 35.9B | other | 563 | 6.2k | 2026-10-01 |
| [qnguyen3/QUAN-Transcribe-1.0](https://huggingface.co/qnguyen3/QUAN-Transcribe-1.0) | automatic-speech-recognition | 0.1B | gemma | 49 | 320 | 2026-10-14 |
| [KaanAydinli/Duyu-small](https://huggingface.co/KaanAydinli/Duyu-small) | automatic-speech-recognition | – | apache-2.0 | 19 | 140 | 2026-10-11 |
| [Jmica/Drama-3-GGUF](https://huggingface.co/Jmica/Drama-3-GGUF) | text-to-speech | – | other | 18 | 133.7k | 2026-10-13 |
| [arbazsiddiqui/voxlock](https://huggingface.co/arbazsiddiqui/voxlock) | audio-to-audio | 0.03B | apache-2.0 | 15 | 200 | 2026-10-11 |
| [PedroMarinhoDev/Drama-3-ComfyUI](https://huggingface.co/PedroMarinhoDev/Drama-3-ComfyUI) | text-to-speech | – | other | 15 | 0 | 2026-10-14 |
| [akhaliq/drama-3-int4](https://huggingface.co/akhaliq/drama-3-int4) | text-to-speech | 6.86B | other | 14 | 437 | 2026-10-13 |
| [TeamUNIVA/qwen3_asr_1.7b_ko](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko) | automatic-speech-recognition | 2.35B | apache-2.0 | 13 | 294 | 2026-10-12 |
| [fishaudio/drama-3-int4](https://huggingface.co/fishaudio/drama-3-int4) | text-to-speech | 6.86B | other | 12 | 954 | 2026-10-14 |
| [IFM/Jais-ASR](https://huggingface.co/IFM/Jais-ASR) | automatic-speech-recognition | 5.72B | apache-2.0 | 9 | 323 | 2026-10-06 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 93 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [LiquidAI/LFM2.5-24B-A2B](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) | text-generation | 23.97B | other | 436 | 9.4k | 2026-10-12 |
| [DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 121 | 14.8k | 2026-09-29 |
| [interfaze-ai/interfaze-1-lite](https://huggingface.co/interfaze-ai/interfaze-1-lite) | image-text-to-text | – | other | 67 | 297 | 2026-10-03 |
| [unsloth/LFM2.5-24B-A2B-GGUF](https://huggingface.co/unsloth/LFM2.5-24B-A2B-GGUF) | text-generation | – | other | 64 | 27.4k | 2026-10-13 |
| [LiquidAI/LFM2.5-24B-A2B-Base](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-Base) | text-generation | 23.97B | other | 36 | 362 | 2026-10-09 |
| [DavidAU/LFM2.5-24B-A2B-Turbo-Brilliance-50X-NEO-MAX-Imatrix-GGUF](https://huggingface.co/DavidAU/LFM2.5-24B-A2B-Turbo-Brilliance-50X-NEO-MAX-Imatrix-GGUF) | text-generation | – | other | 26 | 0 | 2026-10-13 |
| [DavidAU/Qwen3.8-Flash-Next-Abliterated-Uncensored-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-Flash-Next-Abliterated-Uncensored-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-GGUF) | image-text-to-text | – | apache-2.0 | 21 | 9 | 2026-10-15 |
| [DavidAU/Qwen3.8-Flash-Next-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-Flash-Next-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-GGUF) | image-text-to-text | – | apache-2.0 | 19 | 8 | 2026-10-13 |
| [DavidAU/Qwen3.8-Flash-Next-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-Flash-Next-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 10 | 0 | 2026-10-13 |
| [unsloth/LFM2.5-24B-A2B](https://huggingface.co/unsloth/LFM2.5-24B-A2B) | text-generation | 23.97B | other | 6 | 838 | 2026-10-13 |

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
