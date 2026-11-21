# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-21 · catalog size: Vision: 487 · Speech: 472 · LLM Indonesia: 784 · [today's report](reports/2026/11/2026-11-21.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 65 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [thinkingmachines/Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini) | image-text-to-text | 26.39B | apache-2.0 | 1.0k | 136 | 2026-11-17 |
| [harness-hub/Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) | image-text-to-text | – | apache-2.0 | 834 | 1.9k | 2026-11-16 |
| [tencent/Hy4-flash](https://huggingface.co/tencent/Hy4-flash) | image-text-to-text | 220.25B | other | 558 | 3.9k | 2026-11-17 |
| [sensenova/SenseNova-Loop-9B](https://huggingface.co/sensenova/SenseNova-Loop-9B) | image-text-to-text | 9.41B | apache-2.0 | 454 | 1.6k | 2026-11-17 |
| [unsloth/Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF) | image-text-to-text | – | apache-2.0 | 334 | 0 | 2026-11-20 |
| [RadixArk/DaisyRose-27B](https://huggingface.co/RadixArk/DaisyRose-27B) | image-text-to-text | 27.78B | apache-2.0 | 280 | 918 | 2026-11-18 |
| [briaai/RMBG-3.0](https://huggingface.co/briaai/RMBG-3.0) | image-segmentation | 8.13B | other | 259 | 152 | 2026-11-10 |
| [KORMo-VL/KORMo-Web-11B](https://huggingface.co/KORMo-VL/KORMo-Web-11B) | image-text-to-text | 11.19B | apache-2.0 | 239 | 875 | 2026-11-14 |
| [apple/DepthPro2](https://huggingface.co/apple/DepthPro2) | depth-estimation | – | other | 144 | 0 | 2026-11-03 |
| [harness-hub/Qwen3.8-27B-opencode-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-opencode-adapted) | image-text-to-text | – | apache-2.0 | 137 | 302 | 2026-11-16 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 74 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [inworld/voice-isolator](https://huggingface.co/inworld/voice-isolator) | audio-to-audio | – | apache-2.0 | 511 | 0 | 2026-11-14 |
| [n4ze3m/tiny-voca](https://huggingface.co/n4ze3m/tiny-voca) | text-to-speech | – | apache-2.0 | 388 | 7.9k | 2026-11-14 |
| [inworld/sava](https://huggingface.co/inworld/sava) | voice-activity-detection | – | apache-2.0 | 73 | 0 | 2026-11-14 |
| [mehdi-hf/cilla-mini](https://huggingface.co/mehdi-hf/cilla-mini) | text-to-speech | 0.03B | cc-by-nc-4.0 | 62 | 0 | 2026-11-16 |
| [mehdi-hf/cilla-lite](https://huggingface.co/mehdi-hf/cilla-lite) | text-to-speech | 0.11B | cc-by-nc-4.0 | 60 | 0 | 2026-11-14 |
| [sakasegawa/Haru-4B-GGUF](https://huggingface.co/sakasegawa/Haru-4B-GGUF) | audio-to-audio | – | apache-2.0 | 44 | 38.5k | 2026-11-14 |
| [TontaubeAI/TontaubeV1.1-int4](https://huggingface.co/TontaubeAI/TontaubeV1.1-int4) | text-to-speech | – | other | 23 | 0 | 2026-11-10 |
| [drmhse/nano-edge-tts](https://huggingface.co/drmhse/nano-edge-tts) | text-to-speech | – | apache-2.0 | 16 | 314 | 2026-11-11 |
| [ai-coustics/quail-voice-focus](https://huggingface.co/ai-coustics/quail-voice-focus) | audio-to-audio | – | other | 15 | 2.3M | 2026-10-29 |
| [ai-coustics/vad-voice-focus](https://huggingface.co/ai-coustics/vad-voice-focus) | voice-activity-detection | – | other | 15 | 6.4k | 2026-10-29 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 110 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [Peymandc/LFM3-1.7B-Heretic-Uncensored-GGUF](https://huggingface.co/Peymandc/LFM3-1.7B-Heretic-Uncensored-GGUF) | text-generation | – | other | 3 | 1.6k | 2026-11-18 |
| [Peymandc/LFM3-1.7B-Heretic-Uncensored](https://huggingface.co/Peymandc/LFM3-1.7B-Heretic-Uncensored) | text-generation | 1.73B | other | 3 | 420 | 2026-11-17 |
| [prithivMLmods/Domyn-Edge-Teacher-Code-GGUF](https://huggingface.co/prithivMLmods/Domyn-Edge-Teacher-Code-GGUF) | text-generation | – | apache-2.0 | 3 | 0 | 2026-11-20 |
| [mradermacher/LFM3-1.7B-Heretic-Uncensored-i1-GGUF](https://huggingface.co/mradermacher/LFM3-1.7B-Heretic-Uncensored-i1-GGUF) | gguf | – | other | 2 | 2.6k | 2026-11-17 |
| [mradermacher/LFM3-1.7B-Heretic-Uncensored-GGUF](https://huggingface.co/mradermacher/LFM3-1.7B-Heretic-Uncensored-GGUF) | gguf | – | other | 2 | 945 | 2026-11-17 |
| [prithivMLmods/Domyn-Edge-Teacher-Math-GGUF](https://huggingface.co/prithivMLmods/Domyn-Edge-Teacher-Math-GGUF) | text-generation | – | apache-2.0 | 2 | 0 | 2026-11-20 |
| [khbhkb/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/khbhkb/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 1 | 2.0k | 2026-11-17 |
| [ppap2026/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/ppap2026/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 1 | 1.8k | 2026-11-17 |
| [Soulfate24/d1-2B-Paretrix-GGUF](https://huggingface.co/Soulfate24/d1-2B-Paretrix-GGUF) | image-text-to-text | – | other | 1 | 1.6k | 2026-11-15 |
| [mradermacher/Aether-15B-GGUF](https://huggingface.co/mradermacher/Aether-15B-GGUF) | gguf | – | apache-2.0 | 1 | 1.1k | 2026-11-15 |

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
