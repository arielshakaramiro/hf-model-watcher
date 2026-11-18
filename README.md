# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-18 · catalog size: Vision: 449 · Speech: 436 · LLM Indonesia: 729 · [today's report](reports/2026/11/2026-11-18.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 43 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [thinkingmachines/Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small) | image-text-to-text | 383.07B | apache-2.0 | 470 | 18.4k | 2026-11-04 |
| [sensenova/SenseNova-Loop-9B](https://huggingface.co/sensenova/SenseNova-Loop-9B) | image-text-to-text | 9.41B | apache-2.0 | 266 | 0 | 2026-11-17 |
| [harness-hub/Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) | image-text-to-text | – | apache-2.0 | 230 | 0 | 2026-11-16 |
| [nex-agi/Nex-N2.6](https://huggingface.co/nex-agi/Nex-N2.6) | image-text-to-text | 321.32B | apache-2.0 | 157 | 1.1k | 2026-11-10 |
| [tencent/Hy4-flash](https://huggingface.co/tencent/Hy4-flash) | image-text-to-text | 220.25B | other | 119 | 0 | 2026-11-17 |
| [KORMo-VL/KORMo-Web-11B](https://huggingface.co/KORMo-VL/KORMo-Web-11B) | image-text-to-text | 11.19B | apache-2.0 | 95 | 26 | 2026-11-14 |
| [briaai/RMBG-3.0](https://huggingface.co/briaai/RMBG-3.0) | image-segmentation | 8.13B | other | 80 | 0 | 2026-11-10 |
| [iapp/OpenThai2.1-OCR-Markdown-20261118](https://huggingface.co/iapp/OpenThai2.1-OCR-Markdown-20261118) | image-text-to-text | 0.63B | other | 53 | 12.4k | 2026-11-09 |
| [speridlabs/iris-z](https://huggingface.co/speridlabs/iris-z) | depth-estimation | – | other | 52 | 0 | 2026-11-04 |
| [iapp/OpenThai2.0-OCR-Markdown](https://huggingface.co/iapp/OpenThai2.0-OCR-Markdown) | image-text-to-text | 0.63B | other | 50 | 12.1k | 2026-11-09 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 80 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [higurashi-ai/Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B) | audio-to-audio | 5.27B | apache-2.0 | 559 | 4.4k | 2026-11-12 |
| [n4ze3m/tiny-voca](https://huggingface.co/n4ze3m/tiny-voca) | text-to-speech | – | apache-2.0 | 257 | 3.0k | 2026-11-14 |
| [salesforce-sovereign-intelligence/SOV-Transcribe-1](https://huggingface.co/salesforce-sovereign-intelligence/SOV-Transcribe-1) | automatic-speech-recognition | 26.63B | apache-2.0 | 78 | 651 | 2026-11-10 |
| [FluidVoice-Labs/fluid-speech-pro](https://huggingface.co/FluidVoice-Labs/fluid-speech-pro) | automatic-speech-recognition | 0.63B | cc-by-4.0 | 63 | 9.1k | 2026-10-30 |
| [owensong/Inflect-Mini-v3](https://huggingface.co/owensong/Inflect-Mini-v3) | text-to-speech | – | apache-2.0 | 42 | 590 | 2026-11-10 |
| [mehdi-hf/chatterbox-farsi](https://huggingface.co/mehdi-hf/chatterbox-farsi) | text-to-speech | – | other | 38 | 0 | 2026-11-11 |
| [sahilmahendrakar/Earlybird-29M](https://huggingface.co/sahilmahendrakar/Earlybird-29M) | automatic-speech-recognition | – | mit | 33 | 341 | 2026-11-07 |
| [KittenML/kitten-tts-2-mini](https://huggingface.co/KittenML/kitten-tts-2-mini) | text-to-speech | – | apache-2.0 | 30 | 2.8k | 2026-11-13 |
| [mehdi-hf/cilla-lite](https://huggingface.co/mehdi-hf/cilla-lite) | text-to-speech | 0.11B | cc-by-nc-4.0 | 28 | 0 | 2026-11-14 |
| [mehdi-hf/cilla-mini](https://huggingface.co/mehdi-hf/cilla-mini) | text-to-speech | 0.03B | cc-by-nc-4.0 | 26 | 0 | 2026-11-16 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 100 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [translated/Lara-4-Mini-Base](https://huggingface.co/translated/Lara-4-Mini-Base) | text-generation | 7.28B | cc-by-nc-sa-4.0 | 30 | 104 | 2026-11-11 |
| [summerAIO/diffusion-lfm2.5-24b-a2b](https://huggingface.co/summerAIO/diffusion-lfm2.5-24b-a2b) | text-generation | 23.97B | other | 10 | 2.1k | 2026-11-09 |
| [LTM-Lab/Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-ULTRA-HERETIC-Uncensored-v14](https://huggingface.co/LTM-Lab/Qwen3.8-27B-TWIN-TURBO-Fable-Cold-Fusion-709-ULTRA-HERETIC-Uncensored-v14) | image-text-to-text | 27.78B | apache-2.0 | 3 | 182 | 2026-11-10 |
| [K-Ai-Official/Aether-15B](https://huggingface.co/K-Ai-Official/Aether-15B) | text-generation | 14.77B | apache-2.0 | 3 | 112 | 2026-11-14 |
| [mradermacher/Qwen3.8-27B-Ultimate-Heretic-Uncensored-i1-GGUF](https://huggingface.co/mradermacher/Qwen3.8-27B-Ultimate-Heretic-Uncensored-i1-GGUF) | gguf | – | apache-2.0 | 2 | 3.5k | 2026-11-05 |
| [akal-lm/Akal-1B-GGUF](https://huggingface.co/akal-lm/Akal-1B-GGUF) | text-generation | – | gemma | 2 | 215 | 2026-11-13 |
| [Speaks38/Qwen2.5-Coder-1.5B-Python-GGUF](https://huggingface.co/Speaks38/Qwen2.5-Coder-1.5B-Python-GGUF) | gguf | – | apache-2.0 | 2 | 169 | 2026-11-13 |
| [speakleash/Bielik-One-11B-v3.1-r1](https://huggingface.co/speakleash/Bielik-One-11B-v3.1-r1) | text-generation | 11.17B | apache-2.0 | 2 | 150 | 2026-11-10 |
| [Peymandc/LFM3-1.7B-Heretic-Uncensored](https://huggingface.co/Peymandc/LFM3-1.7B-Heretic-Uncensored) | text-generation | 1.73B | other | 2 | 38 | 2026-11-17 |
| [mradermacher/LFM3-1.7B-Heretic-Uncensored-i1-GGUF](https://huggingface.co/mradermacher/LFM3-1.7B-Heretic-Uncensored-i1-GGUF) | gguf | – | other | 2 | 0 | 2026-11-17 |

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
