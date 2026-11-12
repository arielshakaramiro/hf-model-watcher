# HF Model Watcher

A daily, self-updating catalog of new models on the Hugging Face Hub, in three categories:

- **Vision**: image classification, detection, segmentation, depth, vision-language models
- **Speech**: speech recognition, text-to-speech, audio models
- **LLM Indonesia**: every new language model tagged with Indonesian (`id`)

Every morning a GitHub Actions workflow queries the Hub, filters out noise, adds newly found models to a CSV catalog, writes a short daily report, and refreshes the section below.

## Recent additions

<!-- WATCHER_START -->
_Last updated 2026-11-12 · catalog size: Vision: 411 · Speech: 370 · LLM Indonesia: 642 · [today's report](reports/2026/11/2026-11-12.md)_

### Vision

New computer-vision and vision-language models that are already getting attention.

Most-liked of the 38 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [meituan-longcat/LongCat-2.5](https://huggingface.co/meituan-longcat/LongCat-2.5) | image-text-to-text | 1779.75B | mit | 182 | 490 | 2026-11-04 |
| [Cactus-Compute/mirage](https://huggingface.co/Cactus-Compute/mirage) | image-text-to-text | – | apache-2.0 | 180 | 14.6k | 2026-11-05 |
| [fastino/GLiDE-27B](https://huggingface.co/fastino/GLiDE-27B) | image-text-to-text | 26.09B | other | 91 | 2.8k | 2026-10-19 |
| [maritaca-ai/S5-nano](https://huggingface.co/maritaca-ai/S5-nano) | image-text-to-text | 4.66B | apache-2.0 | 76 | 1.2k | 2026-11-02 |
| [nex-agi/Nex-N2.6](https://huggingface.co/nex-agi/Nex-N2.6) | image-text-to-text | 321.32B | apache-2.0 | 48 | 0 | 2026-11-10 |
| [DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF) | image-text-to-text | – | apache-2.0 | 42 | 4.3k | 2026-11-10 |
| [bartowski/NousResearch_Arete-27B-GGUF](https://huggingface.co/bartowski/NousResearch_Arete-27B-GGUF) | image-text-to-text | – | apache-2.0 | 39 | 62.0k | 2026-11-06 |
| [169Pi/Alpie_seed](https://huggingface.co/169Pi/Alpie_seed) | image-text-to-text | 9.41B | apache-2.0 | 25 | 678 | 2026-10-23 |
| [vllm-project/Kimi-K3.1-Pro-pruned75](https://huggingface.co/vllm-project/Kimi-K3.1-Pro-pruned75) | image-text-to-text | 737.61B | other | 22 | 370 | 2026-11-05 |
| [speridlabs/iris-z](https://huggingface.co/speridlabs/iris-z) | depth-estimation | – | other | 22 | 0 | 2026-11-04 |

[Full catalog →](catalog/vision.csv)

### Speech

New speech recognition, text-to-speech and audio models that are already getting attention.

Most-liked of the 57 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [Zyphra/ZONOS3-Mini](https://huggingface.co/Zyphra/ZONOS3-Mini) | text-to-speech | – | apache-2.0 | 200 | 4.2k | 2026-11-09 |
| [ConwayResearch/Underdog-Woof](https://huggingface.co/ConwayResearch/Underdog-Woof) | text-to-speech | – | other | 196 | 10 | 2026-11-05 |
| [Oomni/mithi-v1-flash](https://huggingface.co/Oomni/mithi-v1-flash) | text-to-speech | – | apache-2.0 | 64 | 436 | 2026-11-07 |
| [SyzygyResearch/Mach-Boom](https://huggingface.co/SyzygyResearch/Mach-Boom) | text-to-speech | – | apache-2.0 | 22 | 0 | 2026-11-10 |
| [sahilmahendrakar/Earlybird-29M](https://huggingface.co/sahilmahendrakar/Earlybird-29M) | automatic-speech-recognition | – | mit | 19 | 33 | 2026-11-07 |
| [owensong/Inflect-Mini-v3](https://huggingface.co/owensong/Inflect-Mini-v3) | text-to-speech | – | apache-2.0 | 18 | 0 | 2026-11-10 |
| [mehdi-hf/chatterbox-farsi](https://huggingface.co/mehdi-hf/chatterbox-farsi) | text-to-speech | – | other | 18 | 0 | 2026-11-11 |
| [klein-ml/Klein-TTS-X1.5-Pro](https://huggingface.co/klein-ml/Klein-TTS-X1.5-Pro) | text-to-speech | 0.01B | apache-2.0 | 10 | 236 | 2026-11-03 |
| [goldhub/YuE2-RS-Finetunes](https://huggingface.co/goldhub/YuE2-RS-Finetunes) | text-to-audio | – | cc-by-nc-sa-4.0 | 9 | 12.2k | 2026-10-22 |
| [naklecha/caramel-1](https://huggingface.co/naklecha/caramel-1) | audio-to-audio | 0.41B | apache-2.0 | 8 | 16 | 2026-11-10 |

[Full catalog →](catalog/speech.csv)

### LLM Indonesia

Every new language model tagged with Indonesian (`id`), including base, instruct, GGUF and LoRA releases.

Most-liked of the 141 added in the last 7 days:

| Model | Task | Size | License | ❤️ | ⬇️ | Created |
|-------|------|-----:|---------|---:|---:|---------|
| [DavidAU/Qwen3.8-27B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-27B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF) | image-text-to-text | – | apache-2.0 | 184 | 38.1k | 2026-11-04 |
| [DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF](https://huggingface.co/DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Turbo-Brilliance-50x-AGI-NEO-GGUF) | image-text-to-text | – | apache-2.0 | 42 | 4.3k | 2026-11-10 |
| [DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Build2](https://huggingface.co/DavidAU/Qwen3.8-40B-Ultimate-Heretic-Uncensored-Build2) | image-text-to-text | 39.96B | apache-2.0 | 17 | 1.0k | 2026-11-03 |
| [orcarouter/LFM3-1.7B-abliterated-GGUF](https://huggingface.co/orcarouter/LFM3-1.7B-abliterated-GGUF) | text-generation | – | other | 12 | 374 | 2026-11-05 |
| [speakleash/Bielik-11B-v3.1-Instruct-GGUF](https://huggingface.co/speakleash/Bielik-11B-v3.1-Instruct-GGUF) | gguf | – | apache-2.0 | 7 | 1.1k | 2026-11-10 |
| [summerAIO/diffusion-lfm2.5-24b-a2b](https://huggingface.co/summerAIO/diffusion-lfm2.5-24b-a2b) | text-generation | 23.97B | other | 3 | 1.6k | 2026-11-09 |
| [mradermacher/Mistral-Small-3.2-24B-Instruct-2506-ARA-heretic-i1-GGUF](https://huggingface.co/mradermacher/Mistral-Small-3.2-24B-Instruct-2506-ARA-heretic-i1-GGUF) | gguf | – | apache-2.0 | 2 | 4.8k | 2026-11-06 |
| [mradermacher/Qwen3.8-27B-Uncensored-Impulsive-i1-GGUF](https://huggingface.co/mradermacher/Qwen3.8-27B-Uncensored-Impulsive-i1-GGUF) | gguf | – | apache-2.0 | 2 | 4.1k | 2026-11-05 |
| [mradermacher/Qwen3.8-27B-Ultimate-Heretic-Uncensored-i1-GGUF](https://huggingface.co/mradermacher/Qwen3.8-27B-Ultimate-Heretic-Uncensored-i1-GGUF) | gguf | – | apache-2.0 | 2 | 2.1k | 2026-11-05 |
| [xtools-at/LFM3-1.7B-Claude-Opus-Reasoning-Distilled-GGUF](https://huggingface.co/xtools-at/LFM3-1.7B-Claude-Opus-Reasoning-Distilled-GGUF) | text-generation | – | other | 2 | 1.3k | 2026-11-05 |

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
