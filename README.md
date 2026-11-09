# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-09 · catalog size: Vision: 399 · Speech: 339 · LLM Indonesia: 573 · [today's report](reports/2026/11/2026-11-09.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 50 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [autotrust/Qwen3.8-Flash-Next-E384-FP4-V2](https://huggingface.co/autotrust/Qwen3.8-Flash-Next-E384-FP4-V2) | image-text-to-text | 80.08B | other | 2.4k | 42.7k | 2026-10-26 |
| [moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) | image-text-to-text | 2780.11B | other | 1.7k | 25.6k | 2026-11-02 |
| [ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-Coder-GGUF](https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-Coder-GGUF) | image-text-to-text | – | mit | 206 | 258.7k | 2026-11-02 |
| [RikiyaT/Qwen3.5-0.8B-weight-space-programming](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming) | image-text-to-text | 0.87B | apache-2.0 | 128 | 3.1k | 2026-11-02 |
| [fastino/GLiDE-27B](https://huggingface.co/fastino/GLiDE-27B) | image-text-to-text | 26.09B | other | 86 | 2.4k | 2026-10-19 |
| [Cactus-Compute/mirage](https://huggingface.co/Cactus-Compute/mirage) | image-text-to-text | – | apache-2.0 | 82 | 6.1k | 2026-11-05 |
| [DavidAU/Qwen3.8-27B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF) | image-text-to-text | – | apache-2.0 | 71 | 19.2k | 2026-11-04 |
| [jackjusko/Swift-1.5-Flash-Next-Heretic-ReverseEngineer](https://huggingface.co/jackjusko/Swift-1.5-Flash-Next-Heretic-ReverseEngineer) | image-text-to-text | – | other | 71 | 7.6k | 2026-10-28 |
| [ML-Intern-lab/Qwen3.5-0.8B-weight-space-programming](https://huggingface.co/ML-Intern-lab/Qwen3.5-0.8B-weight-space-programming) | image-text-to-text | 0.87B | apache-2.0 | 68 | 837 | 2026-11-02 |
| [maritaca-ai/S5-nano](https://huggingface.co/maritaca-ai/S5-nano) | image-text-to-text | 4.66B | apache-2.0 | 63 | 419 | 2026-11-02 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 47 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [Edge0/Audio8-TTS-Realistic-Air](https://huggingface.co/Edge0/Audio8-TTS-Realistic-Air) | text-to-speech | 0.6B | apache-2.0 | 369 | 15.3k | 2026-10-14 |
| [ConwayResearch/Underdog-Woof](https://huggingface.co/ConwayResearch/Underdog-Woof) | text-to-speech | – | other | 110 | 10 | 2026-11-05 |
| [pipecat-ai/voice-reader](https://huggingface.co/pipecat-ai/voice-reader) | audio-classification | – | bsd-2-clause | 23 | 89 | 2026-11-02 |
| [Prahaladha/hima-asr](https://huggingface.co/Prahaladha/hima-asr) | automatic-speech-recognition | 0.46B | other | 20 | 573 | 2026-10-12 |
| [Oomni/mithi-v1-flash](https://huggingface.co/Oomni/mithi-v1-flash) | text-to-speech | – | apache-2.0 | 11 | 16 | 2026-11-07 |
| [LocalDoc/speakwrite-azerbaijani](https://huggingface.co/LocalDoc/speakwrite-azerbaijani) | automatic-speech-recognition | – | cc-by-nc-4.0 | 10 | 407 | 2026-11-02 |
| [goldhub/YuE2-RS-Finetunes](https://huggingface.co/goldhub/YuE2-RS-Finetunes) | text-to-audio | – | cc-by-nc-sa-4.0 | 9 | 11.9k | 2026-10-22 |
| [klein-ml/Klein-TTS-X1.5-Pro](https://huggingface.co/klein-ml/Klein-TTS-X1.5-Pro) | text-to-speech | 0.01B | apache-2.0 | 9 | 136 | 2026-11-03 |
| [WhissleAI/steer-tts-nano](https://huggingface.co/WhissleAI/steer-tts-nano) | text-to-speech | – | cc-by-nc-4.0 | 7 | 18 | 2026-11-02 |
| [klein-ml/Klein-TTS-X1.5-Flash-Lite](https://huggingface.co/klein-ml/Klein-TTS-X1.5-Flash-Lite) | text-to-speech | 0B | apache-2.0 | 6 | 230 | 2026-11-03 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 116 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [orcarouter/LFM3-1.7B-abliterated](https://huggingface.co/orcarouter/LFM3-1.7B-abliterated) | text-generation | 1.73B | other | 42 | 479 | 2026-11-02 |
| [orcarouter/LFM3-1.7B-abliterated-GGUF](https://huggingface.co/orcarouter/LFM3-1.7B-abliterated-GGUF) | text-generation | – | other | 7 | 207 | 2026-11-05 |
| [adolan/LFM3-1.7B-abliterated-GGUF](https://huggingface.co/adolan/LFM3-1.7B-abliterated-GGUF) | text-generation | – | other | 3 | 1.0k | 2026-11-02 |
| [xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge](https://huggingface.co/xtools-at/LFM3-1.7B-AgentOrange-Claude-Code-2xMerge) | text-generation | 1.73B | other | 3 | 202 | 2026-11-04 |
| [mradermacher/Qwen3.8-27B-Uncensored-Impulsive-i1-GGUF](https://huggingface.co/mradermacher/Qwen3.8-27B-Uncensored-Impulsive-i1-GGUF) | gguf | – | apache-2.0 | 2 | 4.0k | 2026-11-05 |
| [mradermacher/Mistral-Small-3.2-24B-Instruct-2506-ARA-heretic-i1-GGUF](https://huggingface.co/mradermacher/Mistral-Small-3.2-24B-Instruct-2506-ARA-heretic-i1-GGUF) | gguf | – | apache-2.0 | 2 | 4.0k | 2026-11-06 |
| [xtools-at/LFM3-1.7B-Claude-Opus-Reasoning-Distilled-GGUF](https://huggingface.co/xtools-at/LFM3-1.7B-Claude-Opus-Reasoning-Distilled-GGUF) | text-generation | – | other | 2 | 608 | 2026-11-05 |
| [Shivansh-13929/LFM3-2.2B-Omni-Coder-Instruct](https://huggingface.co/Shivansh-13929/LFM3-2.2B-Omni-Coder-Instruct) | text-generation | 2.17B | other | 2 | 105 | 2026-11-04 |
| [K-Ai-Official/K-Oss-9-Mini](https://huggingface.co/K-Ai-Official/K-Oss-9-Mini) | text-generation | 8.19B | apache-2.0 | 2 | 0 | 2026-11-09 |
| [mradermacher/LFM2.5-24B-A2B-Uncensored-BF16-i1-GGUF](https://huggingface.co/mradermacher/LFM2.5-24B-A2B-Uncensored-BF16-i1-GGUF) | gguf | – | other | 1 | 5.8k | 2026-11-05 |

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
