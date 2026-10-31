# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-10-31 · catalog size: Vision: 342 · Speech: 269 · LLM Indonesia: 424 · [today's report](reports/2026/10/2026-10-31.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 67 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [mistralai/Mistral-Large-4-1T-A52B](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) | image-text-to-text | – | other | 1.2k | 278 | 2026-09-30 |
| [baidu/Unlimited-OCR-2](https://huggingface.co/baidu/Unlimited-OCR-2) | image-text-to-text | 3.34B | mit | 460 | 24.3k | 2026-10-26 |
| [openbmb/MiniCPM-OCR-1.0](https://huggingface.co/openbmb/MiniCPM-OCR-1.0) | image-text-to-text | 1.3B | apache-2.0 | 369 | 2.4k | 2026-10-21 |
| [LiquidAI/LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B) | image-text-to-text | 1.92B | other | 181 | 6.2k | 2026-10-19 |
| [openbmb/MiniCPM-OCR-1.0-gguf](https://huggingface.co/openbmb/MiniCPM-OCR-1.0-gguf) | image-text-to-text | – | apache-2.0 | 128 | 16.1k | 2026-10-21 |
| [LiquidAI/d1-2B](https://huggingface.co/LiquidAI/d1-2B) | image-text-to-text | 1.92B | other | 99 | 2.9k | 2026-10-24 |
| [sensenova/SenseNova-Loop-9B-Preview](https://huggingface.co/sensenova/SenseNova-Loop-9B-Preview) | image-text-to-text | 9.66B | apache-2.0 | 81 | 12 | 2026-10-28 |
| [openbmb/MiniCPM-OCR-Jev](https://huggingface.co/openbmb/MiniCPM-OCR-Jev) | image-text-to-text | 2.21B | apache-2.0 | 79 | 1.4k | 2026-10-23 |
| [huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF) | image-text-to-text | – | mit | 75 | 14.6k | 2026-10-25 |
| [sensenova/SenseNova-6.8-Code2Video](https://huggingface.co/sensenova/SenseNova-6.8-Code2Video) | image-text-to-text | 27.36B | apache-2.0 | 62 | 266 | 2026-10-24 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 59 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) | automatic-speech-recognition | 33.7B | other | 510 | 16.0k | 2026-10-07 |
| [Edge0/Audio8-TTS-Realistic-0.6b](https://huggingface.co/Edge0/Audio8-TTS-Realistic-0.6b) | text-to-speech | 0.6B | apache-2.0 | 126 | 813 | 2026-10-14 |
| [maya-research/maya2-native](https://huggingface.co/maya-research/maya2-native) | text-to-speech | 2.5B | apache-2.0 | 125 | 1.5k | 2026-10-26 |
| [LiquidAI/d1-Omni-2B](https://huggingface.co/LiquidAI/d1-Omni-2B) | audio-text-to-text | 2.17B | other | 83 | 1.1k | 2026-10-24 |
| [ServiceNow-AI/Apriel-Voice-27B-preview](https://huggingface.co/ServiceNow-AI/Apriel-Voice-27B-preview) | audio-text-to-text | 27.23B | mit | 49 | 96 | 2026-10-13 |
| [third-intelligence/Haas-ja-v1.0](https://huggingface.co/third-intelligence/Haas-ja-v1.0) | automatic-speech-recognition | – | apache-2.0 | 28 | 136 | 2026-10-08 |
| [AtomicChat/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF](https://huggingface.co/AtomicChat/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF) | automatic-speech-recognition | – | other | 21 | 20.4k | 2026-10-28 |
| [Aratako/Drama-3-Japanese](https://huggingface.co/Aratako/Drama-3-Japanese) | text-to-speech | 35.9B | other | 20 | 348 | 2026-10-22 |
| [LiquidAI/d1-Omni-2B-GGUF](https://huggingface.co/LiquidAI/d1-Omni-2B-GGUF) | audio-text-to-text | – | other | 19 | 12.4k | 2026-10-27 |
| [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-NVFP4) | automatic-speech-recognition | 18.71B | other | 17 | 1.9k | 2026-10-12 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 127 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) | text-generation | 1.73B | other | 583 | 23.7k | 2026-10-23 |
| [LiquidAI/LFM3-1.7B-GGUF](https://huggingface.co/LiquidAI/LFM3-1.7B-GGUF) | text-generation | – | other | 149 | 97.2k | 2026-10-24 |
| [LiquidAI/LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B) | image-text-to-text | 1.92B | other | 141 | 1.6k | 2026-10-19 |
| [LiquidAI/d1-2B](https://huggingface.co/LiquidAI/d1-2B) | image-text-to-text | 1.92B | other | 99 | 2.9k | 2026-10-24 |
| [LiquidAI/LFM3-1.7B-Base](https://huggingface.co/LiquidAI/LFM3-1.7B-Base) | text-generation | 1.73B | other | 89 | 2.1k | 2026-10-26 |
| [LiquidAI/LFM3-VL-2B-GGUF](https://huggingface.co/LiquidAI/LFM3-VL-2B-GGUF) | image-text-to-text | – | other | 40 | 6.7k | 2026-10-19 |
| [unsloth/Mistral-Large-4-1T-A52B-GGUF](https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-GGUF) | gguf | – | other | 36 | 5.3k | 2026-10-29 |
| [LiquidAI/d1-2B-GGUF](https://huggingface.co/LiquidAI/d1-2B-GGUF) | image-text-to-text | – | other | 25 | 10.1k | 2026-10-27 |
| [LiquidAI/LFM3-1.7B-MLX-4bit](https://huggingface.co/LiquidAI/LFM3-1.7B-MLX-4bit) | text-generation | 1.73B | other | 16 | 4.9k | 2026-10-27 |
| [abenzerps/LFM2.5-24B-A2B-Uncensored-GSQ-RCO-GGUF](https://huggingface.co/abenzerps/LFM2.5-24B-A2B-Uncensored-GSQ-RCO-GGUF) | text-generation | – | other | 15 | 4.0k | 2026-10-27 |

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
