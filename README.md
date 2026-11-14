# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-14 · catalog size: Vision: 422 · Speech: 398 · LLM Indonesia: 674 · [today's report](reports/2026/11/2026-11-14.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 30 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [thinkingmachines/Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small) | image-text-to-text | 383.07B | apache-2.0 | 270 | 1.1k | 2026-11-04 |
| [meituan-longcat/LongCat-2.5](https://huggingface.co/meituan-longcat/LongCat-2.5) | image-text-to-text | 1779.75B | mit | 252 | 971 | 2026-11-04 |
| [nex-agi/Nex-N2.6](https://huggingface.co/nex-agi/Nex-N2.6) | image-text-to-text | 321.32B | apache-2.0 | 77 | 410 | 2026-11-10 |
| [DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF) | image-text-to-text | – | apache-2.0 | 49 | 12.0k | 2026-11-10 |
| [iapp/OpenThai2.0-OCR-Markdown](https://huggingface.co/iapp/OpenThai2.0-OCR-Markdown) | image-text-to-text | 0.63B | other | 35 | 9.2k | 2026-11-09 |
| [speridlabs/iris-z](https://huggingface.co/speridlabs/iris-z) | depth-estimation | – | other | 28 | 0 | 2026-11-04 |
| [Sakura721/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-GGUF](https://huggingface.co/Sakura721/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-GGUF) | image-text-to-text | – | apache-2.0 | 25 | 40.6k | 2026-11-07 |
| [beamster/DeepSeek-V4.1-Flash-1017-Sushi-STQ-1.75bpw](https://huggingface.co/beamster/DeepSeek-V4.1-Flash-1017-Sushi-STQ-1.75bpw) | image-text-to-text | 261.32B | mit | 20 | 3.0k | 2026-10-25 |
| [nvidia/Kimi-K3.1-Pro-NVFP4](https://huggingface.co/nvidia/Kimi-K3.1-Pro-NVFP4) | image-text-to-text | 1418.74B | other | 18 | 620 | 2026-11-11 |
| [169Pi/Alpie_Seed_GGUF](https://huggingface.co/169Pi/Alpie_Seed_GGUF) | image-text-to-text | – | apache-2.0 | 17 | 1.5k | 2026-11-04 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 70 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [Zyphra/ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini) | text-to-speech | – | apache-2.0 | 313 | 13.1k | 2026-11-09 |
| [higurashi-ai/Haru-4B](https://huggingface.co/higurashi-ai/Haru-4B) | audio-to-audio | 5.27B | apache-2.0 | 187 | 165 | 2026-11-12 |
| [Oomni/mithi-v1-flash](https://huggingface.co/Oomni/mithi-v1-flash) | text-to-speech | – | apache-2.0 | 76 | 742 | 2026-11-07 |
| [salesforce-sovereign-intelligence/SOV-Transcribe-1](https://huggingface.co/salesforce-sovereign-intelligence/SOV-Transcribe-1) | automatic-speech-recognition | 26.63B | apache-2.0 | 48 | 184 | 2026-11-10 |
| [sahilmahendrakar/Earlybird-29M](https://huggingface.co/sahilmahendrakar/Earlybird-29M) | automatic-speech-recognition | – | mit | 30 | 144 | 2026-11-07 |
| [mehdi-hf/chatterbox-farsi](https://huggingface.co/mehdi-hf/chatterbox-farsi) | text-to-speech | – | other | 26 | 0 | 2026-11-11 |
| [SyzygyResearch/Mach-Boom](https://huggingface.co/SyzygyResearch/Mach-Boom) | text-to-speech | – | apache-2.0 | 23 | 0 | 2026-11-10 |
| [FluidVoice-Labs/fluid-speech-pro](https://huggingface.co/FluidVoice-Labs/fluid-speech-pro) | automatic-speech-recognition | 0.63B | cc-by-4.0 | 21 | 8.6k | 2026-10-30 |
| [owensong/Inflect-Mini-v3](https://huggingface.co/owensong/Inflect-Mini-v3) | text-to-speech | – | apache-2.0 | 21 | 280 | 2026-11-10 |
| [naklecha/caramel-1](https://huggingface.co/naklecha/caramel-1) | audio-to-audio | 0.41B | apache-2.0 | 17 | 155 | 2026-11-10 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 143 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [DavidAU/Qwen3.8-27B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF) | image-text-to-text | – | apache-2.0 | 193 | 42.3k | 2026-11-04 |
| [DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF) | image-text-to-text | – | apache-2.0 | 49 | 12.0k | 2026-11-10 |
| [translated/Lara-4-Mini-Base](https://huggingface.co/translated/Lara-4-Mini-Base) | text-generation | 7.28B | cc-by-nc-sa-4.0 | 21 | 30 | 2026-11-11 |
| [DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Build2](https://huggingface.co/DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Build2) | image-text-to-text | 39.96B | apache-2.0 | 18 | 1.1k | 2026-11-03 |
| [speakleash/Bielik-11B-v3.1-Instruct-GGUF](https://huggingface.co/speakleash/Bielik-11B-v3.1-Instruct-GGUF) | gguf | – | apache-2.0 | 10 | 2.5k | 2026-11-10 |
| [summerAIO/diffusion-lfm2.5-24b-a2b](https://huggingface.co/summerAIO/diffusion-lfm2.5-24b-a2b) | text-generation | 23.97B | other | 10 | 1.9k | 2026-11-09 |
| [mradermacher/Qwen3.8-27B-Ultimate-Heretic-Uncensored-i1-GGUF](https://huggingface.co/mradermacher/Qwen3.8-27B-Ultimate-Heretic-Uncensored-i1-GGUF) | gguf | – | apache-2.0 | 2 | 2.8k | 2026-11-05 |
| [mradermacher/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF](https://huggingface.co/mradermacher/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF) | gguf | – | other | 2 | 1.1k | 2026-11-08 |
| [mradermacher/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-i1-GGUF](https://huggingface.co/mradermacher/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-i1-GGUF) | gguf | – | other | 2 | 827 | 2026-11-08 |
| [K-Ai-Official/K-Oss-9-Mini](https://huggingface.co/K-Ai-Official/K-Oss-9-Mini) | text-generation | 8.19B | apache-2.0 | 2 | 457 | 2026-11-09 |

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
