# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-10-24 · catalog size: Vision: 275 · Speech: 210 · LLM Indonesia: 297 · [today's report](reports/2026/10/2026-10-24.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 64 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | image-text-to-text | 763.21B | mit | 2.6k | 57.7k | 2026-10-17 |
| [dealignai/DeepSeek-V4.1-Flash-1017-UNCENSORED-FP8](https://huggingface.co/dealignai/DeepSeek-V4.1-Flash-1017-UNCENSORED-FP8) | image-text-to-text | 763.21B | mit | 307 | 4.1k | 2026-10-18 |
| [MiniMaxAI/MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | image-text-to-text | 220.49B | other | 268 | 1.1k | 2026-10-17 |
| [orcarouter/OrcaCyber-Nano-1.0](https://huggingface.co/orcarouter/OrcaCyber-Nano-1.0) | image-text-to-text | – | other | 214 | 22.3k | 2026-10-16 |
| [unsloth/DeepSeek-V4.1-Flash-1017-GGUF](https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF) | image-text-to-text | – | mit | 135 | 29.2k | 2026-10-17 |
| [drowzeys/keys-DeepSeek-V4.1-Flash-1017-Abliterated](https://huggingface.co/drowzeys/keys-DeepSeek-V4.1-Flash-1017-Abliterated) | image-text-to-text | – | mit | 81 | 0 | 2026-10-18 |
| [ATH-MaaS/OvisOCR3](https://huggingface.co/ATH-MaaS/OvisOCR3) | image-text-to-text | 0.85B | apache-2.0 | 59 | 224 | 2026-10-21 |
| [migtissera/Tess-4.5-27B](https://huggingface.co/migtissera/Tess-4.5-27B) | image-text-to-text | 27.78B | apache-2.0 | 51 | 293 | 2026-10-18 |
| [THUSI-Lab/GameScaling](https://huggingface.co/THUSI-Lab/GameScaling) | image-text-to-text | – | apache-2.0 | 45 | 79 | 2026-10-10 |
| [fastino/GLiDE](https://huggingface.co/fastino/GLiDE) | image-text-to-text | 26.09B | other | 41 | 114 | 2026-10-19 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 63 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [gradium/phonon-31m-en](https://huggingface.co/gradium/phonon-31m-en) | text-to-speech | 0.04B | apache-2.0 | 94 | 11.9k | 2026-10-19 |
| [gradium/phonon-40m-en](https://huggingface.co/gradium/phonon-40m-en) | text-to-speech | 0.05B | cc-by-nc-4.0 | 64 | 1.3k | 2026-10-19 |
| [inclusionAI/Ming-3.0-tts-0.5B](https://huggingface.co/inclusionAI/Ming-3.0-tts-0.5B) | text-to-speech | 1.48B | mit | 54 | 1.1k | 2026-09-22 |
| [ibm-granite/granite-speech-5.0-2b](https://huggingface.co/ibm-granite/granite-speech-5.0-2b) | automatic-speech-recognition | 2.31B | apache-2.0 | 48 | 1.1k | 2026-10-07 |
| [gradium/phonon-40m-multilingual](https://huggingface.co/gradium/phonon-40m-multilingual) | text-to-speech | 0.05B | cc-by-nc-4.0 | 45 | 1.5k | 2026-10-19 |
| [inclusionAI/Ming-3.0-asr-tiny](https://huggingface.co/inclusionAI/Ming-3.0-asr-tiny) | automatic-speech-recognition | 8.87B | mit | 41 | 412 | 2026-10-14 |
| [ConwayResearch/Underdog-Bark-3.0](https://huggingface.co/ConwayResearch/Underdog-Bark-3.0) | automatic-speech-recognition | – | cc-by-4.0 | 41 | 103 | 2026-10-15 |
| [AuroraAI-Research/AuroraASR-1M](https://huggingface.co/AuroraAI-Research/AuroraASR-1M) | automatic-speech-recognition | 0B | apache-2.0 | 37 | 221 | 2026-10-18 |
| [ConwayResearch/Underdog-Bark-3.0-Clean](https://huggingface.co/ConwayResearch/Underdog-Bark-3.0-Clean) | automatic-speech-recognition | – | cc-by-4.0 | 37 | 0 | 2026-10-15 |
| [inclusionAI/Ming-3.0-tts-tiny](https://huggingface.co/inclusionAI/Ming-3.0-tts-tiny) | text-to-speech | 8.98B | mit | 29 | 397 | 2026-09-22 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 60 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF](https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF) | text-generation | – | other | 59 | 0 | 2026-10-23 |
| [DavidAU/Qwen3.8-27B-Jumbo-Fusion-IQ-747-900-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Jumbo-Fusion-IQ-747-900-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 39 | 6.8k | 2026-10-18 |
| [mradermacher/LFM2.5-24B-A2B-uncensored-i1-GGUF](https://huggingface.co/mradermacher/LFM2.5-24B-A2B-uncensored-i1-GGUF) | gguf | – | other | 4 | 862 | 2026-10-20 |
| [DavidAU/NVIDIA-Nemotron-3.5-Bolt-E4B-Heretic-Uncensored-Turbo-Brilliance-50x-INST-R-NEO-GGUF](https://huggingface.co/DavidAU/NVIDIA-Nemotron-3.5-Bolt-E4B-Heretic-Uncensored-Turbo-Brilliance-50x-INST-R-NEO-GGUF) | gguf | – | other | 4 | 0 | 2026-10-24 |
| [bartowski/LFM2.5-24B-A2B-GGUF](https://huggingface.co/bartowski/LFM2.5-24B-A2B-GGUF) | text-generation | – | other | 3 | 6.5k | 2026-10-14 |
| [OceanLabs/Coral-2-3B](https://huggingface.co/OceanLabs/Coral-2-3B) | image-text-to-text | 3.12B | other | 3 | 127 | 2026-10-10 |
| [electroglyph/LFM2.5-24B-A2B-uncensored](https://huggingface.co/electroglyph/LFM2.5-24B-A2B-uncensored) | text-generation | 23.97B | other | 2 | 110 | 2026-10-19 |
| [domyn/Domyn-Edge-SFT](https://huggingface.co/domyn/Domyn-Edge-SFT) | text-generation | 3.93B | apache-2.0 | 2 | 108 | 2026-10-13 |
| [mlx-community/NVIDIA-Nemotron-3.5-Bolt-E4B-OptiQ-4bit](https://huggingface.co/mlx-community/NVIDIA-Nemotron-3.5-Bolt-E4B-OptiQ-4bit) | image-text-to-text | 7.46B | other | 2 | 0 | 2026-10-24 |
| [AMAImedia/DeepSeek-V4.1-Flash-1017-FP8-GGUF](https://huggingface.co/AMAImedia/DeepSeek-V4.1-Flash-1017-FP8-GGUF) | image-text-to-text | 763.21B | mit | 1 | 1.9k | 2026-10-17 |

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
