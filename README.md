# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-10-27 · catalog size: Vision: 297 · Speech: 227 · LLM Indonesia: 322 · [today's report](reports/2026/10/2026-10-27.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 61 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [MiniMaxAI/MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | image-text-to-text | 220.49B | other | 389 | 8.8k | 2026-10-17 |
| [baidu/Unlimited-OCR-2](https://huggingface.co/baidu/Unlimited-OCR-2) | image-text-to-text | 3.34B | mit | 77 | 0 | 2026-10-26 |
| [ATH-MaaS/OvisOCR3](https://huggingface.co/ATH-MaaS/OvisOCR3) | image-text-to-text | 0.85B | apache-2.0 | 69 | 904 | 2026-10-21 |
| [tencent/WeVisOne-VL-4B](https://huggingface.co/tencent/WeVisOne-VL-4B) | image-text-to-text | 4.83B | apache-2.0 | 66 | 2.6k | 2026-10-22 |
| [fastino/GLiDE](https://huggingface.co/fastino/GLiDE) | image-text-to-text | 26.09B | other | 57 | 572 | 2026-10-19 |
| [THUSI-Lab/GameScaling](https://huggingface.co/THUSI-Lab/GameScaling) | image-text-to-text | – | apache-2.0 | 55 | 220 | 2026-10-10 |
| [tencent/WeVisOne-VL-2B](https://huggingface.co/tencent/WeVisOne-VL-2B) | image-text-to-text | 2.44B | apache-2.0 | 42 | 2.0k | 2026-10-22 |
| [unsloth/MiniMax-M3.1-Flash-GGUF](https://huggingface.co/unsloth/MiniMax-M3.1-Flash-GGUF) | image-text-to-text | – | other | 37 | 4.5k | 2026-10-23 |
| [nvidia/Flora-Captioner](https://huggingface.co/nvidia/Flora-Captioner) | image-text-to-text | 27.36B | – | 36 | 1.4k | 2026-10-01 |
| [huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF) | image-text-to-text | – | mit | 36 | 127 | 2026-10-25 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 58 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [gradium/phonon-31m-en](https://huggingface.co/gradium/phonon-31m-en) | text-to-speech | 0.04B | apache-2.0 | 115 | 39.5k | 2026-10-19 |
| [gradium/phonon-40m-en](https://huggingface.co/gradium/phonon-40m-en) | text-to-speech | 0.05B | cc-by-nc-4.0 | 78 | 3.8k | 2026-10-19 |
| [ConwayResearch/Underdog-Bark-3.0](https://huggingface.co/ConwayResearch/Underdog-Bark-3.0) | automatic-speech-recognition | – | cc-by-4.0 | 67 | 261 | 2026-10-15 |
| [gradium/phonon-40m-multilingual](https://huggingface.co/gradium/phonon-40m-multilingual) | text-to-speech | 0.05B | cc-by-nc-4.0 | 62 | 3.7k | 2026-10-19 |
| [ConwayResearch/Underdog-Bark-3.0-Clean](https://huggingface.co/ConwayResearch/Underdog-Bark-3.0-Clean) | automatic-speech-recognition | – | cc-by-4.0 | 61 | 0 | 2026-10-15 |
| [ibm-granite/granite-speech-5.0-2b](https://huggingface.co/ibm-granite/granite-speech-5.0-2b) | automatic-speech-recognition | 2.31B | apache-2.0 | 50 | 3.1k | 2026-10-07 |
| [FermionResearch/Phonon-2.5](https://huggingface.co/FermionResearch/Phonon-2.5) | automatic-speech-recognition | – | cc-by-4.0 | 38 | 528 | 2026-10-22 |
| [ConwayResearch/Underdog-Bark-3.0-Pro](https://huggingface.co/ConwayResearch/Underdog-Bark-3.0-Pro) | automatic-speech-recognition | 0.63B | cc-by-4.0 | 36 | 1.1k | 2026-10-15 |
| [alicangunduz/nefes-0.5](https://huggingface.co/alicangunduz/nefes-0.5) | text-to-speech | – | apache-2.0 | 30 | 0 | 2026-10-21 |
| [gradium/phonon-40m-fr](https://huggingface.co/gradium/phonon-40m-fr) | text-to-speech | 0.05B | cc-by-nc-4.0 | 25 | 3.6k | 2026-10-19 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 76 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF](https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF) | text-generation | – | other | 120 | 56.9k | 2026-10-23 |
| [mlx-community/NVIDIA-Nemotron-3.5-Bolt-E4B-OptiQ-4bit](https://huggingface.co/mlx-community/NVIDIA-Nemotron-3.5-Bolt-E4B-OptiQ-4bit) | image-text-to-text | 7.46B | other | 6 | 600 | 2026-10-24 |
| [mradermacher/LFM2.5-24B-A2B-uncensored-i1-GGUF](https://huggingface.co/mradermacher/LFM2.5-24B-A2B-uncensored-i1-GGUF) | gguf | – | other | 4 | 1.7k | 2026-10-20 |
| [DavidAU/NVIDIA-Nemotron-3.5-Bolt-E4B-Heretic-Uncensored-Turbo-Brilliance-50x-INST-R-NEO-GGUF](https://huggingface.co/DavidAU/NVIDIA-Nemotron-3.5-Bolt-E4B-Heretic-Uncensored-Turbo-Brilliance-50x-INST-R-NEO-GGUF) | gguf | – | other | 4 | 0 | 2026-10-24 |
| [bartowski/LFM2.5-24B-A2B-GGUF](https://huggingface.co/bartowski/LFM2.5-24B-A2B-GGUF) | text-generation | – | other | 3 | 8.3k | 2026-10-14 |
| [mradermacher/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16-i1-GGUF](https://huggingface.co/mradermacher/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16-i1-GGUF) | gguf | – | other | 2 | 2.6k | 2026-10-24 |
| [mradermacher/LFM2.5-24B-A2B-uncensored-GGUF](https://huggingface.co/mradermacher/LFM2.5-24B-A2B-uncensored-GGUF) | gguf | – | other | 2 | 506 | 2026-10-20 |
| [domyn/Domyn-Edge-SFT](https://huggingface.co/domyn/Domyn-Edge-SFT) | text-generation | 3.93B | apache-2.0 | 2 | 184 | 2026-10-13 |
| [cc1244578151/Qwen3.8-Flash-Next-Abliterated-Uncensored-GGUF](https://huggingface.co/cc1244578151/Qwen3.8-Flash-Next-Abliterated-Uncensored-GGUF) | image-text-to-text | – | apache-2.0 | 1 | 6.6k | 2026-10-22 |
| [prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF](https://huggingface.co/prithivMLmods/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF) | text-generation | – | other | 1 | 2.0k | 2026-10-24 |

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
