# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-20 · catalog size: Vision: 471 · Speech: 460 · LLM Indonesia: 760 · [today's report](reports/2026/11/2026-11-20.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 52 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [harness-hub/Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) | image-text-to-text | – | apache-2.0 | 765 | 1.3k | 2026-11-16 |
| [sensenova/SenseNova-Loop-9B](https://huggingface.co/sensenova/SenseNova-Loop-9B) | image-text-to-text | 9.41B | apache-2.0 | 400 | 1.4k | 2026-11-17 |
| [tencent/Hy4-flash](https://huggingface.co/tencent/Hy4-flash) | image-text-to-text | 220.25B | other | 385 | 2.1k | 2026-11-17 |
| [RadixArk/DaisyRose-27B](https://huggingface.co/RadixArk/DaisyRose-27B) | image-text-to-text | 27.78B | apache-2.0 | 209 | 166 | 2026-11-18 |
| [briaai/RMBG-3.0](https://huggingface.co/briaai/RMBG-3.0) | image-segmentation | 8.13B | other | 162 | 103 | 2026-11-10 |
| [KORMo-VL/KORMo-Web-11B](https://huggingface.co/KORMo-VL/KORMo-Web-11B) | image-text-to-text | 11.19B | apache-2.0 | 151 | 554 | 2026-11-14 |
| [harness-hub/Qwen3.8-27B-opencode-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-opencode-adapted) | image-text-to-text | – | apache-2.0 | 107 | 124 | 2026-11-16 |
| [KORMo-VL/KORMo-Web-4B](https://huggingface.co/KORMo-VL/KORMo-Web-4B) | image-text-to-text | 5.17B | apache-2.0 | 78 | 374 | 2026-11-14 |
| [KORMo-VL/KORMo-Web-9B](https://huggingface.co/KORMo-VL/KORMo-Web-9B) | image-text-to-text | 9.41B | apache-2.0 | 66 | 445 | 2026-11-14 |
| [sensenova/SenseNova-Loop-9B-GGUF](https://huggingface.co/sensenova/SenseNova-Loop-9B-GGUF) | image-text-to-text | – | apache-2.0 | 62 | 34.3k | 2026-11-18 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 77 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [n4ze3m/tiny-voca](https://huggingface.co/n4ze3m/tiny-voca) | text-to-speech | – | apache-2.0 | 344 | 6.4k | 2026-11-14 |
| [inworld/voice-isolator](https://huggingface.co/inworld/voice-isolator) | audio-to-audio | – | apache-2.0 | 305 | 0 | 2026-11-14 |
| [FluidVoice-Labs/fluid-speech-pro](https://huggingface.co/FluidVoice-Labs/fluid-speech-pro) | automatic-speech-recognition | 0.63B | cc-by-4.0 | 126 | 9.3k | 2026-10-30 |
| [KittenML/kitten-tts-2-mini](https://huggingface.co/KittenML/kitten-tts-2-mini) | text-to-speech | – | apache-2.0 | 64 | 4.9k | 2026-11-13 |
| [inworld/sava](https://huggingface.co/inworld/sava) | voice-activity-detection | – | apache-2.0 | 64 | 0 | 2026-11-14 |
| [mehdi-hf/cilla-mini](https://huggingface.co/mehdi-hf/cilla-mini) | text-to-speech | 0.03B | cc-by-nc-4.0 | 59 | 0 | 2026-11-16 |
| [mehdi-hf/cilla-lite](https://huggingface.co/mehdi-hf/cilla-lite) | text-to-speech | 0.11B | cc-by-nc-4.0 | 58 | 0 | 2026-11-14 |
| [sakasegawa/Haru-4B-GGUF](https://huggingface.co/sakasegawa/Haru-4B-GGUF) | audio-to-audio | – | apache-2.0 | 25 | 36.8k | 2026-11-14 |
| [TontaubeAI/TontaubeV1.1-int4](https://huggingface.co/TontaubeAI/TontaubeV1.1-int4) | text-to-speech | – | other | 22 | 0 | 2026-11-10 |
| [ai-coustics/quail-voice-focus](https://huggingface.co/ai-coustics/quail-voice-focus) | audio-to-audio | – | other | 14 | 1.5M | 2026-10-29 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 103 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [Peymandc/LFM3-1.7B-Heretic-Uncensored](https://huggingface.co/Peymandc/LFM3-1.7B-Heretic-Uncensored) | text-generation | 1.73B | other | 3 | 360 | 2026-11-17 |
| [K-Ai-Official/Aether-15B](https://huggingface.co/K-Ai-Official/Aether-15B) | text-generation | 14.77B | apache-2.0 | 3 | 144 | 2026-11-14 |
| [mradermacher/LFM3-1.7B-Heretic-Uncensored-i1-GGUF](https://huggingface.co/mradermacher/LFM3-1.7B-Heretic-Uncensored-i1-GGUF) | gguf | – | other | 2 | 2.5k | 2026-11-17 |
| [mradermacher/LFM3-1.7B-Heretic-Uncensored-GGUF](https://huggingface.co/mradermacher/LFM3-1.7B-Heretic-Uncensored-GGUF) | gguf | – | other | 2 | 852 | 2026-11-17 |
| [Peymandc/LFM3-1.7B-Heretic-Uncensored-GGUF](https://huggingface.co/Peymandc/LFM3-1.7B-Heretic-Uncensored-GGUF) | text-generation | – | other | 2 | 405 | 2026-11-18 |
| [Speaks38/Qwen2.5-Coder-1.5B-Python-GGUF](https://huggingface.co/Speaks38/Qwen2.5-Coder-1.5B-Python-GGUF) | gguf | – | apache-2.0 | 2 | 259 | 2026-11-13 |
| [khbhkb/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/khbhkb/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 1 | 1.8k | 2026-11-17 |
| [ppap2026/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/ppap2026/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 1 | 1.7k | 2026-11-17 |
| [Soulfate24/d1-2B-Paretrix-GGUF](https://huggingface.co/Soulfate24/d1-2B-Paretrix-GGUF) | image-text-to-text | – | other | 1 | 1.5k | 2026-11-15 |
| [mradermacher/Aether-15B-GGUF](https://huggingface.co/mradermacher/Aether-15B-GGUF) | gguf | – | apache-2.0 | 1 | 942 | 2026-11-15 |

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
