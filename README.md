# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-04 · catalog size: Vision: 363 · Speech: 304 · LLM Indonesia: 488 · [today's report](reports/2026/11/2026-11-04.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 57 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [mistralai/Mistral-Large-4-1T-A52B](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) | image-text-to-text | – | other | 1.2k | 278 | 2026-09-30 |
| [sensenova/SenseNova-Loop-9B-Preview](https://huggingface.co/sensenova/SenseNova-Loop-9B-Preview) | image-text-to-text | 9.66B | apache-2.0 | 215 | 2.2k | 2026-10-28 |
| [microsoft/Mage-VL-Cowork](https://huggingface.co/microsoft/Mage-VL-Cowork) | image-text-to-text | 4.74B | apache-2.0 | 160 | 1.5k | 2026-10-30 |
| [nvidia/DeepSeek-V4.1-Flash-1017-NVFP4](https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4) | image-text-to-text | 664.9B | mit | 149 | 2.9k | 2026-10-30 |
| [openbmb/MiniCPM-OCR-1.0-gguf](https://huggingface.co/openbmb/MiniCPM-OCR-1.0-gguf) | image-text-to-text | – | apache-2.0 | 130 | 27.6k | 2026-10-21 |
| [ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-Coder-GGUF](https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-Coder-GGUF) | image-text-to-text | – | mit | 128 | 28.7k | 2026-11-02 |
| [RikiyaT/Qwen3.5-0.8B-weight-space-programming](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming) | image-text-to-text | 0.87B | apache-2.0 | 75 | 310 | 2026-11-02 |
| [jackjusko/Swift-1.5-Flash-Next-Heretic-ReverseEngineer](https://huggingface.co/jackjusko/Swift-1.5-Flash-Next-Heretic-ReverseEngineer) | image-text-to-text | – | other | 63 | 5.2k | 2026-10-28 |
| [trubisky/Swift-1.5-Flash-Next-Heretic-ReverseEngineer](https://huggingface.co/trubisky/Swift-1.5-Flash-Next-Heretic-ReverseEngineer) | image-text-to-text | – | other | 59 | 3.8k | 2026-10-28 |
| [Jackrong/Qwopus3.8-27B-Coder-Flash-GGUF](https://huggingface.co/Jackrong/Qwopus3.8-27B-Coder-Flash-GGUF) | image-text-to-text | – | apache-2.0 | 57 | 10.6k | 2026-10-28 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 63 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) | automatic-speech-recognition | 33.7B | other | 746 | 38.9k | 2026-10-07 |
| [Edge0/Audio8-TTS-Realistic-Air](https://huggingface.co/Edge0/Audio8-TTS-Realistic-Air) | text-to-speech | 0.6B | apache-2.0 | 279 | 8.1k | 2026-10-14 |
| [ServiceNow-AI/Apriel-Voice-27B-preview](https://huggingface.co/ServiceNow-AI/Apriel-Voice-27B-preview) | audio-text-to-text | 27.23B | mit | 72 | 434 | 2026-10-13 |
| [IrohaStudio/Iroha-TTS](https://huggingface.co/IrohaStudio/Iroha-TTS) | text-to-speech | – | other | 67 | 884 | 2026-10-20 |
| [third-intelligence/Haas-ja-v1.0](https://huggingface.co/third-intelligence/Haas-ja-v1.0) | automatic-speech-recognition | – | apache-2.0 | 56 | 1.5k | 2026-10-08 |
| [empero-ai/PiVo-1.4M](https://huggingface.co/empero-ai/PiVo-1.4M) | text-to-speech | – | apache-2.0 | 40 | 0 | 2026-11-01 |
| [AtomicChat/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF](https://huggingface.co/AtomicChat/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-GGUF) | automatic-speech-recognition | – | other | 34 | 58.2k | 2026-10-28 |
| [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-NVFP4) | automatic-speech-recognition | 18.71B | other | 24 | 7.6k | 2026-10-12 |
| [sahilmahendrakar/Paradee-8M-v1.2](https://huggingface.co/sahilmahendrakar/Paradee-8M-v1.2) | text-to-speech | – | apache-2.0 | 21 | 4.5k | 2026-10-28 |
| [pipecat-ai/voice-reader](https://huggingface.co/pipecat-ai/voice-reader) | audio-classification | – | bsd-2-clause | 20 | 0 | 2026-11-02 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 117 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [unsloth/Mistral-Large-4-1T-A52B-GGUF](https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-GGUF) | gguf | – | other | 47 | 12.7k | 2026-10-29 |
| [orcarouter/LFM3-1.7B-abliterated](https://huggingface.co/orcarouter/LFM3-1.7B-abliterated) | text-generation | 1.73B | other | 31 | 199 | 2026-11-02 |
| [saidutta69/Qwen3.5-4B-heretic](https://huggingface.co/saidutta69/Qwen3.5-4B-heretic) | image-text-to-text | 4.54B | apache-2.0 | 25 | 4.6k | 2026-10-28 |
| [Vortecks/LFM3-1.7B-Heretic-Abliterated-GGUF](https://huggingface.co/Vortecks/LFM3-1.7B-Heretic-Abliterated-GGUF) | text-generation | – | other | 17 | 10.5k | 2026-10-28 |
| [Vortecks/LFM3-1.7B-Heretic-Abliterated](https://huggingface.co/Vortecks/LFM3-1.7B-Heretic-Abliterated) | text-generation | 1.73B | other | 12 | 575 | 2026-10-28 |
| [bartowski/LFM3-1.7B-GGUF](https://huggingface.co/bartowski/LFM3-1.7B-GGUF) | text-generation | – | other | 5 | 4.3k | 2026-10-28 |
| [unsloth/Mistral-Large-4-1T-A52B-FP8](https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-FP8) | image-text-to-text | – | other | 5 | 340 | 2026-10-28 |
| [alexwengg/LFM3-1.7B-Base-MLX-5bit](https://huggingface.co/alexwengg/LFM3-1.7B-Base-MLX-5bit) | text-generation | 1.73B | other | 5 | 240 | 2026-10-28 |
| [Vortecks/LFM3-1.7B-Heretic-Abliterated-i1-GGUF](https://huggingface.co/Vortecks/LFM3-1.7B-Heretic-Abliterated-i1-GGUF) | text-generation | – | other | 4 | 9.2k | 2026-10-28 |
| [saidutta69/LFM3-VL-2B-heretic](https://huggingface.co/saidutta69/LFM3-VL-2B-heretic) | image-text-to-text | 1.92B | other | 4 | 3.9k | 2026-10-28 |

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
