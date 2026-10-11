# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-10-11 · catalog size: Vision: 161 · Speech: 109 · LLM Indonesia: 146 · [today's report](reports/2026/10/2026-10-11.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 54 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [autotrust/GLM5.3-Flash-E224-DGX-Spark](https://huggingface.co/autotrust/GLM5.3-Flash-E224-DGX-Spark) | image-text-to-text | 127.63B | mit | 530 | 5.4k | 2026-10-06 |
| [LiquidAI/d1-3B](https://huggingface.co/LiquidAI/d1-3B) | image-text-to-text | 3.12B | other | 282 | 9.1k | 2026-10-05 |
| [nerkyor/Qwen3.8-27B-Coder390-EfficientThink-Opus5.5-GPT6Astra-Grok4.7-DSV4Pro-K3-SFT-RLOO-MTP-DFlash2](https://huggingface.co/nerkyor/Qwen3.8-27B-Coder390-EfficientThink-Opus5.5-GPT6Astra-Grok4.7-DSV4Pro-K3-SFT-RLOO-MTP-DFlash2) | image-text-to-text | – | apache-2.0 | 208 | 42.3k | 2026-10-04 |
| [LiquidAI/d1-omni-600M](https://huggingface.co/LiquidAI/d1-omni-600M) | image-text-to-text | 0.59B | other | 103 | 10.0k | 2026-10-05 |
| [alesha-pro/Qwen3.8-Flash-Next-abliterated-GSQ-RCO-Strata-GGUF](https://huggingface.co/alesha-pro/Qwen3.8-Flash-Next-abliterated-GSQ-RCO-Strata-GGUF) | image-text-to-text | – | other | 95 | 61.6k | 2026-10-04 |
| [Mia-AiLab/GLM-5.3-Flash-EXL3-4bpw-TensorFold-Ablit](https://huggingface.co/Mia-AiLab/GLM-5.3-Flash-EXL3-4bpw-TensorFold-Ablit) | image-text-to-text | 87.81B | mit | 91 | 3.1k | 2026-10-05 |
| [isichan-ai/Mitsuba_and_HiMitsuba-27B-GGUF](https://huggingface.co/isichan-ai/Mitsuba_and_HiMitsuba-27B-GGUF) | image-text-to-text | – | apache-2.0 | 90 | 16.1k | 2026-09-29 |
| [Cloudflare/clef-omni](https://huggingface.co/Cloudflare/clef-omni) | image-text-to-text | 35.26B | apache-2.0 | 82 | 108 | 2026-10-09 |
| [tencent/Youtu-Parsing-Omni](https://huggingface.co/tencent/Youtu-Parsing-Omni) | image-text-to-text | 5.33B | other | 66 | 340 | 2026-10-09 |
| [lightonai/LightOnOCR-3-4B](https://huggingface.co/lightonai/LightOnOCR-3-4B) | image-text-to-text | 4.54B | apache-2.0 | 65 | 580 | 2026-10-06 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 41 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [canberkkkkkk/ema-lightning](https://huggingface.co/canberkkkkkk/ema-lightning) | text-to-speech | – | apache-2.0 | 347 | 15.7k | 2026-10-01 |
| [neuphonic/neudecide](https://huggingface.co/neuphonic/neudecide) | audio-classification | – | apache-2.0 | 62 | 353 | 2026-10-06 |
| [sahilmahendrakar/Paradee-8M-v1.0](https://huggingface.co/sahilmahendrakar/Paradee-8M-v1.0) | text-to-speech | – | apache-2.0 | 41 | 1.3k | 2026-09-25 |
| [cloud0day3/antalia-mini](https://huggingface.co/cloud0day3/antalia-mini) | text-to-speech | – | apache-2.0 | 30 | 709 | 2026-10-08 |
| [mehdi-hf/pocket-tts-farsi](https://huggingface.co/mehdi-hf/pocket-tts-farsi) | text-to-speech | 0.11B | mit | 30 | 0 | 2026-09-06 |
| [Aratako/Irodori-TTS-v4.1-Small-MF](https://huggingface.co/Aratako/Irodori-TTS-v4.1-Small-MF) | text-to-speech | 0.77B | mit | 16 | 0 | 2026-09-12 |
| [mistralai/Voxtral-Mini-4B-Realtime-Arabic](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-Arabic) | automatic-speech-recognition | 4.43B | – | 14 | 123 | 2026-10-08 |
| [erkamk/qwen3-tts-tiny-tr](https://huggingface.co/erkamk/qwen3-tts-tiny-tr) | text-to-speech | 0.2B | apache-2.0 | 10 | 150 | 2026-10-02 |
| [kova-ai/kova-tts-1](https://huggingface.co/kova-ai/kova-tts-1) | text-to-speech | 1.25B | other | 9 | 652 | 2026-09-23 |
| [ArtShtorm/Shtorm-PocketTTS-RU](https://huggingface.co/ArtShtorm/Shtorm-PocketTTS-RU) | text-to-speech | – | cc-by-4.0 | 9 | 0 | 2026-09-25 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 37 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [LiquidAI/d1-3B](https://huggingface.co/LiquidAI/d1-3B) | image-text-to-text | 3.12B | other | 282 | 9.1k | 2026-10-05 |
| [LiquidAI/d1-3B-GGUF](https://huggingface.co/LiquidAI/d1-3B-GGUF) | image-text-to-text | – | other | 42 | 11.7k | 2026-10-06 |
| [sionic-ai/PepperOCR-VL](https://huggingface.co/sionic-ai/PepperOCR-VL) | image-text-to-text | 4.54B | agpl-3.0 | 7 | 102 | 2026-10-04 |
| [LiquidAI/d1-3B-w8a8](https://huggingface.co/LiquidAI/d1-3B-w8a8) | image-text-to-text | 3.13B | other | 5 | 114 | 2026-10-07 |
| [DJLougen/d1-3B-MLX-8bit](https://huggingface.co/DJLougen/d1-3B-MLX-8bit) | image-text-to-text | 3.12B | other | 3 | 173 | 2026-10-07 |
| [TechnoBaptist/d1-3B-GGUF](https://huggingface.co/TechnoBaptist/d1-3B-GGUF) | image-text-to-text | – | other | 2 | 419 | 2026-10-07 |
| [OceanLabs/Coral-2-3B-fast](https://huggingface.co/OceanLabs/Coral-2-3B-fast) | image-text-to-text | 3.12B | other | 2 | 0 | 2026-10-10 |
| [mradermacher/PepperOCR-VL-GGUF](https://huggingface.co/mradermacher/PepperOCR-VL-GGUF) | gguf | – | agpl-3.0 | 1 | 767 | 2026-10-05 |
| [alekringtonnn-ai/zubr-mini-1.9-3b](https://huggingface.co/alekringtonnn-ai/zubr-mini-1.9-3b) | image-text-to-text | – | apache-2.0 | 1 | 719 | 2026-10-03 |
| [prithivMLmods/d1-3B-GGUF](https://huggingface.co/prithivMLmods/d1-3B-GGUF) | image-text-to-text | – | other | 1 | 608 | 2026-10-07 |

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
