# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-10-28 · catalog size: Vision: 306 · Speech: 241 · LLM Indonesia: 371 · [today's report](reports/2026/10/2026-10-28.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 55 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [MiniMaxAI/MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | image-text-to-text | 220.49B | other | 428 | 11.1k | 2026-10-17 |
| [baidu/Unlimited-OCR-2](https://huggingface.co/baidu/Unlimited-OCR-2) | image-text-to-text | 3.34B | mit | 279 | 513 | 2026-10-26 |
| [openbmb/MiniCPM-OCR-1.0](https://huggingface.co/openbmb/MiniCPM-OCR-1.0) | image-text-to-text | 1.3B | apache-2.0 | 156 | 9 | 2026-10-21 |
| [LiquidAI/LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B) | image-text-to-text | 1.92B | other | 92 | 255 | 2026-10-19 |
| [ATH-MaaS/OvisOCR3](https://huggingface.co/ATH-MaaS/OvisOCR3) | image-text-to-text | 0.85B | apache-2.0 | 79 | 1.6k | 2026-10-21 |
| [tencent/WeVisOne-VL-4B](https://huggingface.co/tencent/WeVisOne-VL-4B) | image-text-to-text | 4.83B | apache-2.0 | 71 | 3.8k | 2026-10-22 |
| [LiquidAI/d1-2B](https://huggingface.co/LiquidAI/d1-2B) | image-text-to-text | 1.92B | other | 61 | 44 | 2026-10-24 |
| [fastino/GLiDE](https://huggingface.co/fastino/GLiDE) | image-text-to-text | 26.09B | other | 60 | 704 | 2026-10-19 |
| [THUSI-Lab/GameScaling](https://huggingface.co/THUSI-Lab/GameScaling) | image-text-to-text | – | apache-2.0 | 57 | 274 | 2026-10-10 |
| [tencent/WeVisOne-VL-2B](https://huggingface.co/tencent/WeVisOne-VL-2B) | image-text-to-text | 2.44B | apache-2.0 | 52 | 3.1k | 2026-10-22 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 58 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [maya-research/maya2-native](https://huggingface.co/maya-research/maya2-native) | text-to-speech | 2.5B | apache-2.0 | 86 | 0 | 2026-10-26 |
| [ConwayResearch/Underdog-Bark-3.0](https://huggingface.co/ConwayResearch/Underdog-Bark-3.0) | automatic-speech-recognition | – | cc-by-4.0 | 77 | 301 | 2026-10-15 |
| [ibm-granite/granite-speech-5.0-2b](https://huggingface.co/ibm-granite/granite-speech-5.0-2b) | automatic-speech-recognition | 2.31B | apache-2.0 | 53 | 3.5k | 2026-10-07 |
| [LiquidAI/d1-Omni-2B](https://huggingface.co/LiquidAI/d1-Omni-2B) | audio-text-to-text | 2.17B | other | 50 | 36 | 2026-10-24 |
| [FermionResearch/Phonon-2.5](https://huggingface.co/FermionResearch/Phonon-2.5) | automatic-speech-recognition | – | cc-by-4.0 | 39 | 651 | 2026-10-22 |
| [alicangunduz/nefes-0.5](https://huggingface.co/alicangunduz/nefes-0.5) | text-to-speech | – | apache-2.0 | 31 | 0 | 2026-10-21 |
| [Edge0/Audio8-TTS-Realistic-0.6b](https://huggingface.co/Edge0/Audio8-TTS-Realistic-0.6b) | text-to-speech | 0.6B | apache-2.0 | 23 | 6 | 2026-10-14 |
| [destined/hurston-1](https://huggingface.co/destined/hurston-1) | text-to-speech | 3.3B | apache-2.0 | 22 | 33 | 2026-10-15 |
| [erayyapagci/balbal-v1](https://huggingface.co/erayyapagci/balbal-v1) | automatic-speech-recognition | – | cc-by-nc-4.0 | 19 | 357 | 2026-10-21 |
| [AuroraAI-Research/AuroraTTS-100K](https://huggingface.co/AuroraAI-Research/AuroraTTS-100K) | text-to-speech | 0B | apache-2.0 | 19 | 332 | 2026-10-22 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 111 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [LiquidAI/LFM3-1.7B](https://huggingface.co/LiquidAI/LFM3-1.7B) | text-generation | 1.73B | other | 233 | 6.3k | 2026-10-23 |
| [unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF](https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF) | text-generation | – | other | 135 | 65.0k | 2026-10-23 |
| [LiquidAI/LFM3-VL-2B](https://huggingface.co/LiquidAI/LFM3-VL-2B) | image-text-to-text | 1.92B | other | 92 | 255 | 2026-10-19 |
| [LiquidAI/LFM3-1.7B-GGUF](https://huggingface.co/LiquidAI/LFM3-1.7B-GGUF) | text-generation | – | other | 63 | 17 | 2026-10-24 |
| [LiquidAI/d1-2B](https://huggingface.co/LiquidAI/d1-2B) | image-text-to-text | 1.92B | other | 61 | 44 | 2026-10-24 |
| [LiquidAI/LFM3-1.7B-Base](https://huggingface.co/LiquidAI/LFM3-1.7B-Base) | text-generation | 1.73B | other | 55 | 15 | 2026-10-26 |
| [LiquidAI/LFM3-VL-2B-GGUF](https://huggingface.co/LiquidAI/LFM3-VL-2B-GGUF) | image-text-to-text | – | other | 27 | 83 | 2026-10-19 |
| [LiquidAI/LFM3-1.7B-MLX-4bit](https://huggingface.co/LiquidAI/LFM3-1.7B-MLX-4bit) | text-generation | 1.73B | other | 10 | 3 | 2026-10-27 |
| [LiquidAI/LFM3-VL-2B-MLX-8bit](https://huggingface.co/LiquidAI/LFM3-VL-2B-MLX-8bit) | image-text-to-text | 1.92B | other | 8 | 8 | 2026-10-22 |
| [LiquidAI/LFM3-VL-2B-ONNX](https://huggingface.co/LiquidAI/LFM3-VL-2B-ONNX) | image-text-to-text | – | other | 8 | 3 | 2026-10-26 |

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
