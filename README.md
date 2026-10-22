# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-10-22 · catalog size: Vision: 261 · Speech: 195 · LLM Indonesia: 269 · [today's report](reports/2026/10/2026-10-22.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 75 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | image-text-to-text | 763.21B | mit | 2.2k | 42.1k | 2026-10-17 |
| [nvidia/Qwen3.8-Flash-Next-FP4-Local](https://huggingface.co/nvidia/Qwen3.8-Flash-Next-FP4-Local) | image-text-to-text | 96.49B | other | 294 | 9.3k | 2026-10-08 |
| [dealignai/DeepSeek-V4.1-Flash-1017-UNCENSORED-FP8](https://huggingface.co/dealignai/DeepSeek-V4.1-Flash-1017-UNCENSORED-FP8) | image-text-to-text | 763.21B | mit | 213 | 3.5k | 2026-10-18 |
| [nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4) | image-text-to-text | 65.77B | other | 205 | 12.9k | 2026-10-12 |
| [orcarouter/OrcaCyber-Nano-1.0](https://huggingface.co/orcarouter/OrcaCyber-Nano-1.0) | image-text-to-text | – | other | 175 | 19.7k | 2026-10-16 |
| [nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB) | image-text-to-text | 22.37B | other | 145 | 7.5k | 2026-10-07 |
| [unsloth/DeepSeek-V4.1-Flash-1017-GGUF](https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF) | image-text-to-text | – | mit | 123 | 18.8k | 2026-10-17 |
| [prism-ml/Ternary-Bonsai-2-9B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-9B-gguf) | image-text-to-text | – | apache-2.0 | 116 | 96.5k | 2026-09-23 |
| [nvidia/GLM-5.3-Flash-FP4-Local](https://huggingface.co/nvidia/GLM-5.3-Flash-FP4-Local) | image-text-to-text | 175.24B | other | 113 | 3.5k | 2026-10-08 |
| [nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF) | image-text-to-text | – | other | 106 | 92.8k | 2026-10-07 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 61 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [nineninesix/tyger](https://huggingface.co/nineninesix/tyger) | automatic-speech-recognition | 0.65B | openmdw-1.1 | 81 | 502 | 2026-10-12 |
| [gradium/phonon-31m-en](https://huggingface.co/gradium/phonon-31m-en) | text-to-speech | 0.04B | apache-2.0 | 72 | 3.6k | 2026-10-19 |
| [inclusionAI/Ming-3.0-tts-0.5B](https://huggingface.co/inclusionAI/Ming-3.0-tts-0.5B) | text-to-speech | 1.48B | mit | 54 | 1.1k | 2026-09-22 |
| [gradium/phonon-40m-en](https://huggingface.co/gradium/phonon-40m-en) | text-to-speech | 0.05B | cc-by-nc-4.0 | 54 | 562 | 2026-10-19 |
| [inclusionAI/Ming-3.0-asr-tiny](https://huggingface.co/inclusionAI/Ming-3.0-asr-tiny) | automatic-speech-recognition | 8.87B | mit | 36 | 274 | 2026-10-14 |
| [gradium/phonon-40m-multilingual](https://huggingface.co/gradium/phonon-40m-multilingual) | text-to-speech | 0.05B | cc-by-nc-4.0 | 35 | 349 | 2026-10-19 |
| [AuroraAI-Research/AuroraASR-1M](https://huggingface.co/AuroraAI-Research/AuroraASR-1M) | automatic-speech-recognition | 0B | apache-2.0 | 34 | 165 | 2026-10-18 |
| [ConwayResearch/Underdog-Bark-3.0-Clean](https://huggingface.co/ConwayResearch/Underdog-Bark-3.0-Clean) | automatic-speech-recognition | – | cc-by-4.0 | 32 | 0 | 2026-10-15 |
| [ibm-granite/granite-speech-5.0-2b](https://huggingface.co/ibm-granite/granite-speech-5.0-2b) | automatic-speech-recognition | 2.31B | apache-2.0 | 31 | 105 | 2026-10-07 |
| [inclusionAI/Ming-3.0-tts-tiny](https://huggingface.co/inclusionAI/Ming-3.0-tts-tiny) | text-to-speech | 8.98B | mit | 29 | 397 | 2026-09-22 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 60 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [DavidAU/Qwen3.8-Flash-Next-Abliterated-Uncensored-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-Flash-Next-Abliterated-Uncensored-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-GGUF) | image-text-to-text | – | apache-2.0 | 62 | 24.1k | 2026-10-15 |
| [DavidAU/Qwen3.8-27B-Jumbo-Fusion-IQ-747-900-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Jumbo-Fusion-IQ-747-900-Turbo-Brilliance-50X-Reasoning-Instruct-NEO-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 34 | 5.3k | 2026-10-18 |
| [DavidAU/Qwen3.8-Flash-Next-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-Flash-Next-Turbo-Brilliance-50x-Reasoning-Instruct-GSQ-RCO-GGUF) | image-text-to-text | – | apache-2.0 | 31 | 8.1k | 2026-10-13 |
| [mradermacher/LFM2.5-24B-A2B-uncensored-i1-GGUF](https://huggingface.co/mradermacher/LFM2.5-24B-A2B-uncensored-i1-GGUF) | gguf | – | other | 4 | 379 | 2026-10-20 |
| [OceanLabs/Coral-2-3B](https://huggingface.co/OceanLabs/Coral-2-3B) | image-text-to-text | 3.12B | other | 3 | 126 | 2026-10-10 |
| [prithivMLmods/LiquidAI-LFM2.5-24B-A2B-GGUF](https://huggingface.co/prithivMLmods/LiquidAI-LFM2.5-24B-A2B-GGUF) | text-generation | – | other | 2 | 529 | 2026-10-15 |
| [ai-toba/toba-multilingual-3.5B](https://huggingface.co/ai-toba/toba-multilingual-3.5B) | text-generation | 3.52B | – | 2 | 332 | 2026-10-15 |
| [electroglyph/LFM2.5-24B-A2B-uncensored](https://huggingface.co/electroglyph/LFM2.5-24B-A2B-uncensored) | text-generation | 23.97B | other | 2 | 88 | 2026-10-19 |
| [domyn/Domyn-Edge-SFT](https://huggingface.co/domyn/Domyn-Edge-SFT) | text-generation | 3.93B | apache-2.0 | 2 | 63 | 2026-10-13 |
| [mradermacher/LFM2.5-24B-A2B-Uncensored-Heretic-i1-GGUF](https://huggingface.co/mradermacher/LFM2.5-24B-A2B-Uncensored-Heretic-i1-GGUF) | gguf | – | other | 1 | 5.0k | 2026-10-17 |

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
