# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-10-08 · catalog size: Vision: 136 · Speech: 98 · LLM Indonesia: 135 · [today's report](reports/2026/10/2026-10-08.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 52 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [autotrust/JEV-27B-VL](https://huggingface.co/autotrust/JEV-27B-VL) | image-text-to-text | 27.78B | apache-2.0 | 2.3k | 1.5M | 2026-09-30 |
| [Cloudflare/clef](https://huggingface.co/Cloudflare/clef) | image-text-to-text | 27.36B | apache-2.0 | 1.8k | 9.5k | 2026-09-30 |
| [Cloudflare/clef-flash](https://huggingface.co/Cloudflare/clef-flash) | image-text-to-text | 9.41B | apache-2.0 | 670 | 15.7k | 2026-09-30 |
| [SC117/Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF](https://huggingface.co/SC117/Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF) | image-text-to-text | – | apache-2.0 | 143 | 500.7k | 2026-10-02 |
| [LiquidAI/d1-3B](https://huggingface.co/LiquidAI/d1-3B) | image-text-to-text | 3.12B | other | 120 | 15 | 2026-10-05 |
| [autotrust/GLM5.3-Flash-E224-DGX-Spark](https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark) | image-text-to-text | 127.63B | mit | 104 | 68 | 2026-10-06 |
| [isichan-ai/Mitsuba_and_HiMitsuba-27B-GGUF](https://huggingface.co/isichan-ai/Mitsuba_and_HiMitsuba-27B-GGUF) | image-text-to-text | – | apache-2.0 | 90 | 16.1k | 2026-09-29 |
| [alesha-pro/Qwen3.8-Flash-Next-abliterated-GSQ-RCO-Strata-GGUF](https://huggingface.co/alesha-pro/Qwen3.8-Flash-Next-abliterated-GSQ-RCO-Strata-GGUF) | image-text-to-text | – | other | 74 | 15.1k | 2026-10-04 |
| [Mia-AiLab/GLM-5.3-Flash-EXL3-4bpw-TensorFold-Ablit](https://huggingface.co/Mia-AiLab/GLM-5.3-Flash-EXL3-4bpw-TensorFold-Ablit) | image-text-to-text | 87.81B | mit | 60 | 1.8k | 2026-10-05 |
| [LiquidAI/d1-omni-600M](https://huggingface.co/LiquidAI/d1-omni-600M) | image-text-to-text | 0.59B | other | 53 | 28 | 2026-10-05 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 43 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [canberkkkkkk/ema-lightning](https://huggingface.co/canberkkkkkk/ema-lightning) | text-to-speech | – | apache-2.0 | 278 | 2.7k | 2026-10-01 |
| [Cactus-Compute/whistle](https://huggingface.co/Cactus-Compute/whistle) | automatic-speech-recognition | – | apache-2.0 | 151 | 2.2k | 2026-09-30 |
| [rumik-ai/rumik-oss-1](https://huggingface.co/rumik-ai/rumik-oss-1) | text-to-speech | 3.38B | cc-by-nc-4.0 | 64 | 2.6k | 2026-09-06 |
| [mehdi-hf/pocket-tts-farsi-v2](https://huggingface.co/mehdi-hf/pocket-tts-farsi-v2) | text-to-speech | 0.11B | cc-by-nc-4.0 | 35 | 0 | 2026-09-12 |
| [mehdi-hf/pocket-tts-farsi](https://huggingface.co/mehdi-hf/pocket-tts-farsi) | text-to-speech | 0.11B | mit | 30 | 0 | 2026-09-06 |
| [KittenML/kitten-tts-2](https://huggingface.co/KittenML/kitten-tts-2) | text-to-speech | – | other | 25 | 2.2k | 2026-09-30 |
| [sahilmahendrakar/Paradee-8M-v1.0](https://huggingface.co/sahilmahendrakar/Paradee-8M-v1.0) | text-to-speech | – | apache-2.0 | 19 | 86 | 2026-09-25 |
| [Aratako/Irodori-TTS-v4.1-Small-MF](https://huggingface.co/Aratako/Irodori-TTS-v4.1-Small-MF) | text-to-speech | 0.77B | mit | 16 | 0 | 2026-09-12 |
| [mehdi-hf/nemotron-asr-streaming-farsi](https://huggingface.co/mehdi-hf/nemotron-asr-streaming-farsi) | automatic-speech-recognition | 0.62B | other | 14 | 980 | 2026-10-03 |
| [BuzzASR/persian](https://huggingface.co/BuzzASR/persian) | automatic-speech-recognition | 1.55B | mit | 12 | 1.1k | 2026-09-08 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 46 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [LiquidAI/d1-3B](https://huggingface.co/LiquidAI/d1-3B) | image-text-to-text | 3.12B | other | 120 | 15 | 2026-10-05 |
| [LiquidAI/d1-3B-GGUF](https://huggingface.co/LiquidAI/d1-3B-GGUF) | image-text-to-text | – | other | 27 | 22 | 2026-10-06 |
| [DavidAU/LFM2.5-8B-A1B-Qwen3.8-Turbo-Brilliance-Power-X12-NEO-MAX-GGUF](https://huggingface.co/DavidAU/LFM2.5-8B-A1B-Qwen3.8-Turbo-Brilliance-Power-X12-NEO-MAX-GGUF) | text-generation | – | apache-2.0 | 21 | 6.9k | 2026-10-02 |
| [sionic-ai/PepperOCR-VL](https://huggingface.co/sionic-ai/PepperOCR-VL) | image-text-to-text | 4.54B | agpl-3.0 | 5 | 74 | 2026-10-04 |
| [AneekC/quipu-moe-1B-A149M](https://huggingface.co/AneekC/quipu-moe-1B-A149M) | text-generation | 1B | apache-2.0 | 2 | 120 | 2026-10-02 |
| [LiquidAI/d1-3B-w8a8](https://huggingface.co/LiquidAI/d1-3B-w8a8) | image-text-to-text | 3.13B | other | 2 | 0 | 2026-10-07 |
| [TechnoBaptist/d1-3B-GGUF](https://huggingface.co/TechnoBaptist/d1-3B-GGUF) | image-text-to-text | – | other | 2 | 0 | 2026-10-07 |
| [mradermacher/PepperOCR-VL-GGUF](https://huggingface.co/mradermacher/PepperOCR-VL-GGUF) | gguf | – | agpl-3.0 | 1 | 696 | 2026-10-05 |
| [alekringtonnn-ai/zubr-mini-1.9-3b](https://huggingface.co/alekringtonnn-ai/zubr-mini-1.9-3b) | image-text-to-text | – | apache-2.0 | 1 | 538 | 2026-10-03 |
| [alekringtonnn-ai/zubr-tiny-2b](https://huggingface.co/alekringtonnn-ai/zubr-tiny-2b) | text-generation | – | apache-2.0 | 1 | 512 | 2026-10-01 |

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
