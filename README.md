# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-19 · catalog size: Vision: 458 · Speech: 449 · LLM Indonesia: 742 · [today's report](reports/2026/11/2026-11-19.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 47 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [harness-hub/Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) | image-text-to-text | – | apache-2.0 | 644 | 377 | 2026-11-16 |
| [thinkingmachines/Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small) | image-text-to-text | 383.07B | apache-2.0 | 553 | 30.1k | 2026-11-04 |
| [sensenova/SenseNova-Loop-9B](https://huggingface.co/sensenova/SenseNova-Loop-9B) | image-text-to-text | 9.41B | apache-2.0 | 350 | 964 | 2026-11-17 |
| [tencent/Hy4-flash](https://huggingface.co/tencent/Hy4-flash) | image-text-to-text | 220.25B | other | 271 | 159 | 2026-11-17 |
| [KORMo-VL/KORMo-Web-11B](https://huggingface.co/KORMo-VL/KORMo-Web-11B) | image-text-to-text | 11.19B | apache-2.0 | 116 | 277 | 2026-11-14 |
| [RadixArk/DaisyRose-27B](https://huggingface.co/RadixArk/DaisyRose-27B) | image-text-to-text | 27.78B | apache-2.0 | 115 | 0 | 2026-11-18 |
| [briaai/RMBG-3.0](https://huggingface.co/briaai/RMBG-3.0) | image-segmentation | 8.13B | other | 113 | 42 | 2026-11-10 |
| [KORMo-VL/KORMo-Web-4B](https://huggingface.co/KORMo-VL/KORMo-Web-4B) | image-text-to-text | 5.17B | apache-2.0 | 71 | 212 | 2026-11-14 |
| [iapp/OpenThai2.1-OCR-Markdown-20261118](https://huggingface.co/iapp/OpenThai2.1-OCR-Markdown-20261118) | image-text-to-text | 0.63B | other | 56 | 12.5k | 2026-11-09 |
| [sensenova/SenseNova-Loop-9B-GGUF](https://huggingface.co/sensenova/SenseNova-Loop-9B-GGUF) | image-text-to-text | – | apache-2.0 | 52 | 0 | 2026-11-18 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 79 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [higurashi-ai/Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B) | audio-to-audio | 5.27B | apache-2.0 | 1.4k | 5.3k | 2026-11-12 |
| [n4ze3m/tiny-voca](https://huggingface.co/n4ze3m/tiny-voca) | text-to-speech | – | apache-2.0 | 304 | 4.4k | 2026-11-14 |
| [inworld/voice-isolator](https://huggingface.co/inworld/voice-isolator) | audio-to-audio | – | apache-2.0 | 135 | 0 | 2026-11-14 |
| [salesforce-sovereign-intelligence/SOV-Transcribe-1](https://huggingface.co/salesforce-sovereign-intelligence/SOV-Transcribe-1) | automatic-speech-recognition | 26.63B | apache-2.0 | 91 | 735 | 2026-11-10 |
| [FluidVoice-Labs/fluid-speech-pro](https://huggingface.co/FluidVoice-Labs/fluid-speech-pro) | automatic-speech-recognition | 0.63B | cc-by-4.0 | 89 | 9.2k | 2026-10-30 |
| [mehdi-hf/cilla-lite](https://huggingface.co/mehdi-hf/cilla-lite) | text-to-speech | 0.11B | cc-by-nc-4.0 | 42 | 0 | 2026-11-14 |
| [KittenML/kitten-tts-2-mini](https://huggingface.co/KittenML/kitten-tts-2-mini) | text-to-speech | – | apache-2.0 | 37 | 3.9k | 2026-11-13 |
| [mehdi-hf/cilla-mini](https://huggingface.co/mehdi-hf/cilla-mini) | text-to-speech | 0.03B | cc-by-nc-4.0 | 37 | 0 | 2026-11-16 |
| [inworld/sava](https://huggingface.co/inworld/sava) | voice-activity-detection | – | apache-2.0 | 25 | 0 | 2026-11-14 |
| [VoxDance-Lab/VoxMel-0.6B](https://huggingface.co/VoxDance-Lab/VoxMel-0.6B) | text-to-speech | – | apache-2.0 | 23 | 318 | 2026-11-10 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 100 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [translated/Lara-4-Mini-Base](https://huggingface.co/translated/Lara-4-Mini-Base) | text-generation | 7.28B | cc-by-nc-sa-4.0 | 32 | 123 | 2026-11-11 |
| [Peymandc/LFM3-1.7B-Heretic-Uncensored](https://huggingface.co/Peymandc/LFM3-1.7B-Heretic-Uncensored) | text-generation | 1.73B | other | 3 | 314 | 2026-11-17 |
| [K-Ai-Official/Aether-15B](https://huggingface.co/K-Ai-Official/Aether-15B) | text-generation | 14.77B | apache-2.0 | 3 | 136 | 2026-11-14 |
| [mradermacher/LFM3-1.7B-Heretic-Uncensored-GGUF](https://huggingface.co/mradermacher/LFM3-1.7B-Heretic-Uncensored-GGUF) | gguf | – | other | 2 | 398 | 2026-11-17 |
| [akal-lm/Akal-1B-GGUF](https://huggingface.co/akal-lm/Akal-1B-GGUF) | text-generation | – | gemma | 2 | 351 | 2026-11-13 |
| [mradermacher/LFM3-1.7B-Heretic-Uncensored-i1-GGUF](https://huggingface.co/mradermacher/LFM3-1.7B-Heretic-Uncensored-i1-GGUF) | gguf | – | other | 2 | 309 | 2026-11-17 |
| [Speaks38/Qwen2.5-Coder-1.5B-Python-GGUF](https://huggingface.co/Speaks38/Qwen2.5-Coder-1.5B-Python-GGUF) | gguf | – | apache-2.0 | 2 | 240 | 2026-11-13 |
| [speakleash/Bielik-One-11B-v3.1-r1](https://huggingface.co/speakleash/Bielik-One-11B-v3.1-r1) | text-generation | 11.17B | apache-2.0 | 2 | 177 | 2026-11-10 |
| [Peymandc/LFM3-1.7B-Heretic-Uncensored-GGUF](https://huggingface.co/Peymandc/LFM3-1.7B-Heretic-Uncensored-GGUF) | text-generation | – | other | 2 | 0 | 2026-11-18 |
| [khbhkb/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/khbhkb/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 1 | 1.7k | 2026-11-17 |

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
