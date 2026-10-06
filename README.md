# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-10-06 · catalog size: Vision: 123 · Speech: 82 · LLM Indonesia: 118 · [today's report](reports/2026/10/2026-10-06.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 123 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | image-text-to-text | 763.21B | mit | 4.1k | 869.3k | 2026-09-10 |
| [TaichuAI/ZDTaichu5.0-9B](https://huggingface.co/TaichuAI/ZDTaichu5.0-9B) | image-text-to-text | 9.79B | – | 2.8k | 12.5k | 2026-09-04 |
| [Cloudflare/clef](https://huggingface.co/Cloudflare/clef) | image-text-to-text | 27.36B | apache-2.0 | 1.5k | 5.4k | 2026-09-30 |
| [autotrust/JEV-27B-VL](https://huggingface.co/autotrust/JEV-27B-VL) | image-text-to-text | 27.78B | apache-2.0 | 804 | 1.3M | 2026-09-30 |
| [ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF) | image-text-to-text | – | apache-2.0 | 625 | 2.2M | 2026-09-07 |
| [ukisai/Swift-Qwen3.8-27b](https://huggingface.co/ukisai/Swift-Qwen3.8-27b) | image-text-to-text | 27.78B | other | 615 | 22.3k | 2026-09-08 |
| [XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B) | image-text-to-text | 9.41B | mit | 615 | 16.2k | 2026-09-21 |
| [Cloudflare/clef-flash](https://huggingface.co/Cloudflare/clef-flash) | image-text-to-text | 9.41B | apache-2.0 | 548 | 8.1k | 2026-09-30 |
| [ukisai/Swift-Qwen3.8-27B-GGUF](https://huggingface.co/ukisai/Swift-Qwen3.8-27B-GGUF) | image-text-to-text | – | other | 453 | 362.2k | 2026-09-11 |
| [PSRben/VisionHOPE](https://huggingface.co/PSRben/VisionHOPE) | image-classification | – | mit | 426 | 1.7k | 2026-09-29 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 82 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [Edge0/Audio8-ASR-Infinite](https://huggingface.co/Edge0/Audio8-ASR-Infinite) | automatic-speech-recognition | 4.09B | apache-2.0 | 2.4k | 40.1k | 2026-09-21 |
| [m-a-p/YuE2-3B](https://huggingface.co/m-a-p/YuE2-3B) | text-to-audio | 3.63B | cc-by-nc-4.0 | 1.1k | 34.1k | 2026-09-09 |
| [nvidia/Nemotron-3-Diarization](https://huggingface.co/nvidia/Nemotron-3-Diarization) | voice-activity-detection | 0.1B | openmdw-1.1 | 572 | 36.4k | 2026-09-01 |
| [netease-youdao/Confucius4-R2T2](https://huggingface.co/netease-youdao/Confucius4-R2T2) | automatic-speech-recognition | 2.04B | other | 521 | 17.5k | 2026-09-10 |
| [microsoft/VibeVoice-ASR-Streaming-7B](https://huggingface.co/microsoft/VibeVoice-ASR-Streaming-7B) | automatic-speech-recognition | 8.67B | mit | 250 | 7.0k | 2026-09-02 |
| [FermionResearch/Phonon-2](https://huggingface.co/FermionResearch/Phonon-2) | automatic-speech-recognition | – | cc-by-4.0 | 238 | 3.1k | 2026-09-28 |
| [moondream/parakeet-redux](https://huggingface.co/moondream/parakeet-redux) | automatic-speech-recognition | 0.15B | cc-by-4.0 | 232 | 10.2k | 2026-09-18 |
| [Cactus-Compute/whistle](https://huggingface.co/Cactus-Compute/whistle) | automatic-speech-recognition | – | apache-2.0 | 111 | 1.4k | 2026-09-30 |
| [oruk/orukeet](https://huggingface.co/oruk/orukeet) | automatic-speech-recognition | 0.63B | cc-by-sa-4.0 | 97 | 36.7k | 2026-09-09 |
| [audio-cpp/Yue2-3B-GGUF](https://huggingface.co/audio-cpp/Yue2-3B-GGUF) | text-to-audio | – | cc-by-nc-4.0 | 90 | 166.3k | 2026-09-10 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 118 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [DavidAU/LFM2.5-2.6B-Qwen3.8-Turbo-Brilliance-Power-X12-NEO-MAX-GGUF](https://huggingface.co/DavidAU/LFM2.5-2.6B-Qwen3.8-Turbo-Brilliance-Power-X12-NEO-MAX-GGUF) | text-generation | – | apache-2.0 | 142 | 23.0k | 2026-09-17 |
| [DavidAU/Qwen3.8-27B-Turbo-Brilliance-Power-35X-Reasoning-Instruct-modes-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Turbo-Brilliance-Power-35X-Reasoning-Instruct-modes-GGUF) | image-text-to-text | – | apache-2.0 | 53 | 0 | 2026-09-29 |
| [hiwaifu-research/WaifuGemma4-26b-a4b-v1](https://huggingface.co/hiwaifu-research/WaifuGemma4-26b-a4b-v1) | text-generation | 25.81B | apache-2.0 | 23 | 1.5k | 2026-09-18 |
| [DavidAU/LFM2.5-8B-A1B-Qwen3.8-Turbo-Brilliance-Power-X12-NEO-MAX-GGUF](https://huggingface.co/DavidAU/LFM2.5-8B-A1B-Qwen3.8-Turbo-Brilliance-Power-X12-NEO-MAX-GGUF) | text-generation | – | apache-2.0 | 15 | 5.0k | 2026-10-02 |
| [monotykamary/LFM2.5-2.6B-RLCD](https://huggingface.co/monotykamary/LFM2.5-2.6B-RLCD) | text-generation | 2.7B | other | 7 | 779 | 2026-09-16 |
| [hiwaifu-research/WaifuGemma4-26b-a4b-v1-i1-GGUF](https://huggingface.co/hiwaifu-research/WaifuGemma4-26b-a4b-v1-i1-GGUF) | text-generation | – | apache-2.0 | 6 | 9.0k | 2026-09-18 |
| [sionic-ai/PepperOCR-VL](https://huggingface.co/sionic-ai/PepperOCR-VL) | image-text-to-text | 4.54B | agpl-3.0 | 5 | 12 | 2026-10-04 |
| [CohereLabs/tiny-aya-base-32K](https://huggingface.co/CohereLabs/tiny-aya-base-32K) | text-generation | 3.35B | cc-by-nc-4.0 | 4 | 9 | 2026-09-08 |
| [DahonoLabs/Dahono-4B](https://huggingface.co/DahonoLabs/Dahono-4B) | image-text-to-text | 4.66B | apache-2.0 | 3 | 2.4k | 2026-09-13 |
| [hiwaifu-research/WaifuGemma4-26b-a4b-v1-GGUF](https://huggingface.co/hiwaifu-research/WaifuGemma4-26b-a4b-v1-GGUF) | text-generation | – | apache-2.0 | 2 | 1.3k | 2026-09-18 |

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
