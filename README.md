# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-24 · catalog size: Vision: 519 · Speech: 506 · LLM Indonesia: 809 · [today's report](reports/2026/11/2026-11-24.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 80 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [thinkingmachines/Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini) | image-text-to-text | 26.39B | apache-2.0 | 5.6k | 69.0k | 2026-11-17 |
| [unsloth/Inkling-2-Mini-GGUF](https://huggingface.co/unsloth/Inkling-2-Mini-GGUF) | image-text-to-text | – | apache-2.0 | 1.2k | 1.9M | 2026-11-20 |
| [apple/DepthPro2](https://huggingface.co/apple/DepthPro2) | depth-estimation | – | other | 1.2k | 0 | 2026-11-03 |
| [harness-hub/Qwen3.8-27B-pi-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) | image-text-to-text | – | apache-2.0 | 1.1k | 3.5k | 2026-11-16 |
| [AtomicChat/Inkling-2-Mini-Uncensored-GGUF](https://huggingface.co/AtomicChat/Inkling-2-Mini-Uncensored-GGUF) | image-text-to-text | – | apache-2.0 | 692 | 573.8k | 2026-11-20 |
| [tencent/Hy4-flash](https://huggingface.co/tencent/Hy4-flash) | image-text-to-text | 220.25B | other | 664 | 9.2k | 2026-11-17 |
| [sensenova/SenseNova-Loop-9B](https://huggingface.co/sensenova/SenseNova-Loop-9B) | image-text-to-text | 9.41B | apache-2.0 | 659 | 2.7k | 2026-11-17 |
| [RadixArk/DaisyRose-27B](https://huggingface.co/RadixArk/DaisyRose-27B) | image-text-to-text | 27.78B | apache-2.0 | 348 | 2.5k | 2026-11-18 |
| [tencent/Hy4](https://huggingface.co/tencent/Hy4) | image-text-to-text | 774.43B | other | 288 | 2.4k | 2026-10-29 |
| [harness-hub/Qwen3.8-27B-opencode-adapted](https://huggingface.co/harness-hub/Qwen3.8-27B-opencode-adapted) | image-text-to-text | – | apache-2.0 | 284 | 972 | 2026-11-16 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 77 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [inworld/voice-isolator](https://huggingface.co/inworld/voice-isolator) | audio-to-audio | – | apache-2.0 | 768 | 12.7k | 2026-11-14 |
| [adventists-ai/Sophon-Realtime-v1](https://huggingface.co/adventists-ai/Sophon-Realtime-v1) | audio-to-audio | – | apache-2.0 | 260 | 33 | 2026-11-07 |
| [inworld/sava](https://huggingface.co/inworld/sava) | voice-activity-detection | – | apache-2.0 | 107 | 1.8k | 2026-11-14 |
| [StudioYebisu-ship-it/Drama-3-Japanese-speech-cpp-gguf](https://huggingface.co/StudioYebisu-ship-it/Drama-3-Japanese-speech-cpp-gguf) | text-to-speech | – | other | 32 | 4.5k | 2026-11-23 |
| [adventists-ai/Sophon-Realtime-4B-Flash](https://huggingface.co/adventists-ai/Sophon-Realtime-4B-Flash) | audio-to-audio | – | apache-2.0 | 21 | 933 | 2026-11-16 |
| [ai-coustics/quail-voice-focus](https://huggingface.co/ai-coustics/quail-voice-focus) | audio-to-audio | – | other | 20 | 4.5M | 2026-10-29 |
| [KaleComputer/kale-tts-1-nano](https://huggingface.co/KaleComputer/kale-tts-1-nano) | text-to-speech | – | apache-2.0 | 19 | 410 | 2026-11-16 |
| [ai-coustics/quail-multi-speaker](https://huggingface.co/ai-coustics/quail-multi-speaker) | audio-to-audio | – | other | 17 | 4.3k | 2026-10-29 |
| [ai-coustics/rook-multi-speaker](https://huggingface.co/ai-coustics/rook-multi-speaker) | audio-to-audio | – | other | 17 | 3.9k | 2026-10-29 |
| [ai-coustics/vad-voice-focus](https://huggingface.co/ai-coustics/vad-voice-focus) | voice-activity-detection | – | other | 16 | 13.2k | 2026-10-29 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 96 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [Peymandc/LFM3-1.7B-Heretic-Uncensored-GGUF](https://huggingface.co/Peymandc/LFM3-1.7B-Heretic-Uncensored-GGUF) | text-generation | – | other | 5 | 2.7k | 2026-11-18 |
| [mradermacher/LFM3-1.7B-Heretic-Uncensored-i1-GGUF](https://huggingface.co/mradermacher/LFM3-1.7B-Heretic-Uncensored-i1-GGUF) | gguf | – | other | 3 | 2.9k | 2026-11-17 |
| [mradermacher/LFM3-1.7B-Heretic-Uncensored-GGUF](https://huggingface.co/mradermacher/LFM3-1.7B-Heretic-Uncensored-GGUF) | gguf | – | other | 3 | 1.2k | 2026-11-17 |
| [prithivMLmods/Domyn-Edge-Teacher-Math-GGUF](https://huggingface.co/prithivMLmods/Domyn-Edge-Teacher-Math-GGUF) | text-generation | – | apache-2.0 | 3 | 639 | 2026-11-20 |
| [prithivMLmods/Domyn-Edge-Teacher-Code-GGUF](https://huggingface.co/prithivMLmods/Domyn-Edge-Teacher-Code-GGUF) | text-generation | – | apache-2.0 | 3 | 637 | 2026-11-20 |
| [khbhkb/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF](https://huggingface.co/khbhkb/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF) | image-text-to-text | – | apache-2.0 | 1 | 2.2k | 2026-11-17 |
| [KiyoEditz/Elaina-gemma-4-31B-v0.1-GGUF](https://huggingface.co/KiyoEditz/Elaina-gemma-4-31B-v0.1-GGUF) | text-generation | – | other | 1 | 853 | 2026-11-19 |
| [prithivMLmods/Domyn-Edge-SFT-GGUF](https://huggingface.co/prithivMLmods/Domyn-Edge-SFT-GGUF) | text-generation | – | apache-2.0 | 1 | 653 | 2026-11-20 |
| [prithivMLmods/Domyn-Edge-Teacher-IF-GGUF](https://huggingface.co/prithivMLmods/Domyn-Edge-Teacher-IF-GGUF) | text-generation | – | apache-2.0 | 1 | 575 | 2026-11-20 |
| [prithivMLmods/Domyn-Edge-Teacher-Agentic-GGUF](https://huggingface.co/prithivMLmods/Domyn-Edge-Teacher-Agentic-GGUF) | text-generation | – | apache-2.0 | 1 | 544 | 2026-11-20 |

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
