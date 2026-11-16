# Medux API Examples

Complete API-first examples generated from the [official Medux API Reference](https://medux.io/api-reference/).

The REST API does not differ between Claude, Codex, or other clients. Each of the **68 APIs** has one canonical example containing its contract, curl command, runnable Python and JavaScript clients, response handling, official sample data, and optional MCP mapping.

## Prerequisites

- A Medux API key — see [docs/authentication.md](./docs/authentication.md).
- Python 3.9+ (for `example.py`) and/or Node.js 18+ (for `example.mjs`).
- `curl` and `bash` (for `curl.sh`).

New to the API? Read [docs/concepts.md](./docs/concepts.md) first: it covers the
upload flow, the asynchronous task lifecycle, credits, and pagination that the
per-endpoint pages assume.

## Quick start

```bash
git clone https://github.com/MeduxIO/medux-api-examples.git
cd medux-api-examples
cp .env.example .env            # then edit .env with your key
export MEDUX_API_KEY="your_api_key"
python3 -m pip install -r requirements.txt
```

Choose an API below. For Python and JavaScript, set the placeholder environment variables documented in its README; set `MEDUX_API_BASE_URL` only to target a non-production host. For curl, replace the uppercase placeholders inline before running `curl.sh`.

## API catalog


### Get Started

| API | Method | Endpoint |
| --- | --- | --- |
| [Create Upload URL](./examples/get-started/create-upload-url/) | `POST` | `/api/app/v1/upload_urls` |

### Clone

| API | Method | Endpoint |
| --- | --- | --- |
| [Create Avatar by Image](./examples/clone/create-avatar-by-image/) | `POST` | `/api/app/v1/clone/avatar/by_image` |
| [Create Avatar by Video](./examples/clone/create-avatar-by-video/) | `POST` | `/api/app/v1/clone/avatar/by_video` |
| [Create Voice](./examples/clone/create-voice/) | `POST` | `/api/app/v1/clone/voice` |
| [Edit Voice Parameters](./examples/clone/edit-voice-parameters/) | `POST` | `/api/app/v1/clone/voice/{voice_asset_id}/parameters` |
| [Get Avatar Task](./examples/clone/get-avatar-task/) | `GET` | `/api/app/v1/clone/avatar/tasks/{task_id}` |
| [Get Voice Task](./examples/clone/get-voice-task/) | `GET` | `/api/app/v1/clone/voice/tasks/{task_id}` |
| [List Avatars](./examples/clone/list-avatars/) | `GET` | `/api/app/v1/clone/avatars` |
| [List Voices](./examples/clone/list-voices/) | `GET` | `/api/app/v1/clone/voices` |

### Generate

| API | Method | Endpoint |
| --- | --- | --- |
| [Create Audio](./examples/generate/create-audio/) | `POST` | `/api/app/v1/generate/audio` |
| [Create Audio Driven Video](./examples/generate/create-audio-driven-video/) | `POST` | `/api/app/v1/generate/video/audio_driven` |
| [Create Image to Video](./examples/generate/create-image-to-video/) | `POST` | `/api/app/v1/generate/video/image_to_video` |
| [Create Text Driven Video](./examples/generate/create-text-driven-video/) | `POST` | `/api/app/v1/generate/video/text_driven` |
| [Create Text to Video](./examples/generate/create-text-to-video/) | `POST` | `/api/app/v1/generate/video/text_to_video` |
| [Create Video by Project](./examples/generate/create-video-by-project/) | `POST` | `/api/app/v1/generate/video/by_project` |
| [Get Creation Task](./examples/generate/get-creation-task/) | `GET` | `/api/app/v1/generate/tasks/{task_id}` |
| [Create Text to Image](./examples/generate/text-to-image/) | `POST` | `/api/app/v1/generate/image/text_to_image` |
| [Create Image Audio Driven Video](./examples/generate/image-audio-driven-video/) | `POST` | `/api/app/v1/generate/video/image_audio_driven` |

### Infra

| API | Method | Endpoint |
| --- | --- | --- |
| [Create Asset](./examples/infra/create-asset/) | `POST` | `/api/app/v1/assets` |
| [Get Task](./examples/infra/get-task/) | `GET` | `/api/app/v1/tasks/{task_id}` |
| [List Assets](./examples/infra/list-assets/) | `GET` | `/api/app/v1/assets` |
| [List Results](./examples/infra/list-results/) | `GET` | `/api/app/v1/results` |
| [List Tasks](./examples/infra/list-tasks/) | `GET` | `/api/app/v1/tasks` |
| [Sync Task](./examples/infra/sync-task/) | `POST` | `/api/app/v1/tasks/{task_id}/sync` |

### Process

| API | Method | Endpoint |
| --- | --- | --- |
| [Create Image Background Removal](./examples/process/create-image-background-removal/) | `POST` | `/api/app/v1/process/image/background_removal` |
| [Create Video Background Removal](./examples/process/create-video-background-removal/) | `POST` | `/api/app/v1/process/video/background_removal` |
| [Create Video Subtitle Removal](./examples/process/create-video-subtitle-removal/) | `POST` | `/api/app/v1/process/video/subtitle_removal` |
| [Create Video Watermark Removal](./examples/process/create-video-watermark-removal/) | `POST` | `/api/app/v1/process/video/watermark_removal` |
| [Get Process Task](./examples/process/get-process-task/) | `GET` | `/api/app/v1/process/tasks/{task_id}` |
| [Create Video Logo Removal](./examples/process/video-logo-removal/) | `POST` | `/api/app/v1/process/video/video_logo_removal` |

### Edit

| API | Method | Endpoint |
| --- | --- | --- |
| [Image Face Swap](./examples/edit/face-swap/) | `POST` | `/api/app/v1/process/image/face_swap` |
| [Image Head Swap](./examples/edit/head-swap/) | `POST` | `/api/app/v1/process/image/head_swap` |
| [Image Outfit Swap](./examples/edit/outfit-swap/) | `POST` | `/api/app/v1/process/image/outfit_swap` |
| [Video Character Replacement](./examples/edit/character-replacement/) | `POST` | `/api/app/v1/process/video/character_replacement` |
| [Remove Video Object](./examples/edit/remove-video-object/) | `POST` | `/api/app/v1/process/video/remove_video_object` |
| [Photo Repair](./examples/edit/photo-repair/) | `POST` | `/api/app/v1/process/image/photo_repair` |
| [Video Upscale](./examples/edit/video-upscale/) | `POST` | `/api/app/v1/process/video/video_upscale` |
| [Video Head Swap](./examples/edit/video-head-swap/) | `POST` | `/api/app/v1/process/video/animate_head_swap` |

### Media

| API | Method | Endpoint |
| --- | --- | --- |
| [Trim Video](./examples/media/trim-video/) | `POST` | `/api/app/v1/process/video/trim_video` |
| [Split Video](./examples/media/split-video/) | `POST` | `/api/app/v1/process/video/split_video` |
| [Merge Video](./examples/media/merge-video/) | `POST` | `/api/app/v1/process/video/merge_video` |
| [Resize Video](./examples/media/resize-video/) | `POST` | `/api/app/v1/process/video/resize_video` |
| [Rotate Video](./examples/media/rotate-video/) | `POST` | `/api/app/v1/process/video/rotate_video` |
| [Flip Video](./examples/media/flip-video/) | `POST` | `/api/app/v1/process/video/flip_video` |
| [Change Video Speed](./examples/media/change-video-speed/) | `POST` | `/api/app/v1/process/video/change_video_speed` |
| [Adjust Video Volume](./examples/media/adjust-video-volume/) | `POST` | `/api/app/v1/process/video/adjust_video_volume` |
| [Add Audio to Video](./examples/media/add-audio-to-video/) | `POST` | `/api/app/v1/process/video/add_audio_to_video` |
| [Add Logo to Video](./examples/media/add-logo-to-video/) | `POST` | `/api/app/v1/process/video/add_logo_to_video` |
| [Trim Audio](./examples/media/trim-audio/) | `POST` | `/api/app/v1/process/audio/trim_audio` |
| [Merge Audio](./examples/media/merge-audio/) | `POST` | `/api/app/v1/process/audio/merge_audio` |
| [Reverse Audio](./examples/media/reverse-audio/) | `POST` | `/api/app/v1/process/audio/reverse_audio` |
| [Change Audio Speed](./examples/media/change-audio-speed/) | `POST` | `/api/app/v1/process/audio/change_audio_speed` |
| [Adjust Audio Volume](./examples/media/adjust-audio-volume/) | `POST` | `/api/app/v1/process/audio/adjust_audio_volume` |
| [Shift Audio Pitch](./examples/media/shift-audio-pitch/) | `POST` | `/api/app/v1/process/audio/shift_audio_pitch` |

### Document

| API | Method | Endpoint |
| --- | --- | --- |
| [Word to PDF](./examples/document/word-to-pdf/) | `POST` | `/api/app/v1/process/asset/word_to_pdf` |
| [Excel to PDF](./examples/document/excel-to-pdf/) | `POST` | `/api/app/v1/process/asset/excel_to_pdf` |
| [PPT to PDF](./examples/document/ppt-to-pdf/) | `POST` | `/api/app/v1/process/asset/ppt_to_pdf` |
| [PDF to Word](./examples/document/pdf-to-word/) | `POST` | `/api/app/v1/process/asset/pdf_to_word` |
| [PDF to DOCX](./examples/document/pdf-to-docx/) | `POST` | `/api/app/v1/process/asset/pdf_to_docx` |
| [PDF to Excel](./examples/document/pdf-to-excel/) | `POST` | `/api/app/v1/process/asset/pdf_to_excel` |
| [PDF to PPT](./examples/document/pdf-to-ppt/) | `POST` | `/api/app/v1/process/asset/pdf_to_ppt` |
| [PDF to Images](./examples/document/pdf-to-images/) | `POST` | `/api/app/v1/process/asset/pdf_to_images` |
| [PDF to JPG](./examples/document/pdf-to-jpg/) | `POST` | `/api/app/v1/process/asset/pdf_to_jpg` |
| [PDF to PNG](./examples/document/pdf-to-png/) | `POST` | `/api/app/v1/process/asset/pdf_to_png` |
| [Images to PDF](./examples/document/images-to-pdf/) | `POST` | `/api/app/v1/process/asset/images_to_pdf` |
| [JPG/PNG to PDF](./examples/document/jpg-png-to-pdf/) | `POST` | `/api/app/v1/process/asset/jpg_png_to_pdf` |
| [Merge PDF](./examples/document/merge-pdf/) | `POST` | `/api/app/v1/process/asset/merge_pdf` |
| [Split PDF](./examples/document/split-pdf/) | `POST` | `/api/app/v1/process/asset/split_pdf` |

## Repository layout

```text
examples/<module>/<endpoint>/
├── README.md       # Complete endpoint guide
├── curl.sh         # Copy-ready official curl request
├── example.py      # Python client
├── example.mjs     # Node.js client
├── request.json    # Official request body example
└── reference.json  # Structured endpoint reference
```

## Refreshing from the official reference

```bash
python3 scripts/fetch_api_reference.py
python3 scripts/generate_examples.py
python3 scripts/validate_examples.py
```

The committed `api-reference.json` is a reviewable snapshot of the public reference used to generate the repository.

## Documentation

- [docs/authentication.md](./docs/authentication.md) — prerequisites, API key, and environment variables.
- [docs/concepts.md](./docs/concepts.md) — files vs. assets, upload flow, async task lifecycle, credits, and pagination.
- [docs/error-codes.md](./docs/error-codes.md) — the consolidated response-code catalog and retry guidance.

## Security

Never commit API keys, private asset IDs, private media URLs, or user data. Store credentials in environment variables and review requests before sending them.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
