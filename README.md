# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-05 · catalog size: Vision: 373 · Speech: 313 · LLM Indonesia: 501 · [today's report](reports/2026/11/2026-11-05.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 54 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [mistralai/Mistral-Large-4-1T-A52B](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) | image-text-to-text | – | other | 1.2k | 278 | 2026-09-30 |
| [autotrust/Qwen3.8-Flash-Next-E384-FP4-V2](https://huggingface.co/autotrust/Qwen3.8-Flash-Next-E384-FP4-V2) | image-text-to-text | 80.08B | other | 1.1k | 26.5k | 2026-10-26 |
| [moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) | image-text-to-text | 2780.11B | other | 654 | 797 | 2026-11-02 |
| [sensenova/SenseNova-Loop-9B-Preview](https://huggingface.co/sensenova/SenseNova-Loop-9B-Preview) | image-text-to-text | 9.66B | apache-2.0 | 241 | 2.7k | 2026-10-28 |
| [microsoft/Mage-VL-Cowork](https://huggingface.co/microsoft/Mage-VL-Cowork) | image-text-to-text | 4.74B | apache-2.0 | 183 | 2.0k | 2026-10-30 |
| [nvidia/DeepSeek-V4.1-Flash-1017-NVFP4](https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4) | image-text-to-text | 664.9B | mit | 178 | 3.6k | 2026-10-30 |
| [ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-Coder-GGUF](https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-Coder-GGUF) | image-text-to-text | – | mit | 166 | 73.3k | 2026-11-02 |
| [RikiyaT/Qwen3.5-0.8B-weight-space-programming](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming) | image-text-to-text | 0.87B | apache-2.0 | 99 | 1.3k | 2026-11-02 |
| [jackjusko/Swift-1.5-Flash-Next-Heretic-ReverseEngineer](https://huggingface.co/jackjusko/Swift-1.5-Flash-Next-Heretic-ReverseEngineer) | image-text-to-text | – | other | 68 | 6.0k | 2026-10-28 |
| [Jackrong/Qwopus3.8-27B-Coder-Flash-GGUF](https://huggingface.co/Jackrong/Qwopus3.8-27B-Coder-Flash-GGUF) | image-text-to-text | – | apache-2.0 | 59 | 14.4k | 2026-10-28 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 64 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [Edge0/Audio8-TTS-Realistic-Air](https://huggingface.co/Edge0/Audio8-TTS-Realistic-Air) | text-to-speech | 0.6B | apache-2.0 | 302 | 9.7k | 2026-10-14 |
| [IrohaStudio/Iroha-TTS](https://huggingface.co/IrohaStudio/Iroha-TTS) | text-to-speech | – | other | 77 | 1.1k | 2026-10-20 |
| [ServiceNow-AI/Apriel-Voice-27B-preview](https://huggingface.co/ServiceNow-AI/Apriel-Voice-27B-preview) | audio-text-to-text | 27.23B | mit | 77 | 571 | 2026-10-13 |
| [third-intelligence/Haas-ja-v1.0](https://huggingface.co/third-intelligence/Haas-ja-v1.0) | automatic-speech-recognition | – | apache-2.0 | 59 | 1.8k | 2026-10-08 |
| [empero-ai/PiVo-1.4M](https://huggingface.co/empero-ai/PiVo-1.4M) | text-to-speech | – | apache-2.0 | 43 | 0 | 2026-11-01 |
| [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B-NVFP4) | automatic-speech-recognition | 18.71B | other | 28 | 8.9k | 2026-10-12 |
| [pipecat-ai/voice-reader](https://huggingface.co/pipecat-ai/voice-reader) | audio-classification | – | bsd-2-clause | 20 | 0 | 2026-11-02 |
| [erayyapagci/balbal-v2-manas](https://huggingface.co/erayyapagci/balbal-v2-manas) | automatic-speech-recognition | – | other | 16 | 234 | 2026-10-29 |
| [BlueRoseLabs/Silencio-2](https://huggingface.co/BlueRoseLabs/Silencio-2) | text-to-speech | 0.03B | cc-by-4.0 | 16 | 150 | 2026-10-31 |
| [AlmawaveLabs/Velvet2-3B-Speech](https://huggingface.co/AlmawaveLabs/Velvet2-3B-Speech) | audio-text-to-text | 4.55B | apache-2.0 | 15 | 145 | 2026-10-23 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 104 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [unsloth/Mistral-Large-4-1T-A52B-GGUF](https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-GGUF) | gguf | – | other | 47 | 14.2k | 2026-10-29 |
| [orcarouter/LFM3-1.7B-abliterated](https://huggingface.co/orcarouter/LFM3-1.7B-abliterated) | text-generation | 1.73B | other | 36 | 337 | 2026-11-02 |
| [unsloth/Mistral-Large-4-1T-A52B-FP8](https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-FP8) | image-text-to-text | – | other | 5 | 407 | 2026-10-28 |
| [ReStranger/LFM3-1.7B-Claude-Code-Abliterated-GGUF](https://huggingface.co/ReStranger/LFM3-1.7B-Claude-Code-Abliterated-GGUF) | text-generation | – | other | 4 | 892 | 2026-10-31 |
| [adolan/LFM3-1.7B-abliterated-GGUF](https://huggingface.co/adolan/LFM3-1.7B-abliterated-GGUF) | text-generation | – | other | 3 | 616 | 2026-11-02 |
| [MihaiPopa-1/LFM3-1.7B-Heretic-Max](https://huggingface.co/MihaiPopa-1/LFM3-1.7B-Heretic-Max) | text-generation | 1.73B | other | 2 | 760 | 2026-10-30 |
| [unsloth/Mistral-Large-4-1T-A52B-NVFP4](https://huggingface.co/unsloth/Mistral-Large-4-1T-A52B-NVFP4) | – | – | other | 2 | 40 | 2026-10-27 |
| [MihaiPopa-1/LFM3-1.7B-Heretic-Max-LoRA](https://huggingface.co/MihaiPopa-1/LFM3-1.7B-Heretic-Max-LoRA) | text-generation | – | other | 2 | 0 | 2026-10-30 |
| [xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge](https://huggingface.co/xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge) | text-generation | 1.73B | other | 2 | 0 | 2026-11-04 |
| [cybertruck32489/LFM3-1.7B-RD](https://huggingface.co/cybertruck32489/LFM3-1.7B-RD) | text-generation | 1.69B | other | 1 | 3.4k | 2026-10-31 |

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
