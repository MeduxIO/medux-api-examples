# Medux API Examples

Complete API-first examples generated from the [official Medux API Reference](https://medux.io/api-reference/).

The REST API does not differ between Claude, Codex, or other clients. Each of the **74 APIs** has one canonical example containing its contract, curl command, runnable Python and JavaScript clients, response handling, official sample data, and optional MCP mapping.

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


### Clone

| API | Method | Endpoint |
| --- | --- | --- |
| [Clone Avatar by Image](./examples/clone/create-avatar-by-image/) | `POST` | `/api/app/v1/clone/avatar/by_image` |
| [Clone Avatar by Video](./examples/clone/create-avatar-by-video/) | `POST` | `/api/app/v1/clone/avatar/by_video` |
| [List Avatars](./examples/clone/list-avatars/) | `GET` | `/api/app/v1/clone/avatars` |
| [Clone Voice](./examples/clone/create-voice/) | `POST` | `/api/app/v1/clone/voice` |
| [Edit Voice Parameters](./examples/clone/edit-voice-parameters/) | `POST` | `/api/app/v1/clone/voice/{voice_asset_id}/parameters` |
| [List Voices](./examples/clone/list-voices/) | `GET` | `/api/app/v1/clone/voices` |

### Generate

| API | Method | Endpoint |
| --- | --- | --- |
| [Audio Driven Video](./examples/generate/create-audio-driven-video/) | `POST` | `/api/app/v1/generate/video/audio_driven` |
| [Text Driven Video](./examples/generate/create-text-driven-video/) | `POST` | `/api/app/v1/generate/video/text_driven` |
| [Text to Video](./examples/generate/create-text-to-video/) | `POST` | `/api/app/v1/generate/video/text_to_video` |
| [Image to Video](./examples/generate/create-image-to-video/) | `POST` | `/api/app/v1/generate/video/image_to_video` |
| [First and Last Frame to Video](./examples/generate/create-first-last-frame-to-video/) | `POST` | `/api/app/v1/generate/video/first_last_frame_to_video` |
| [Omni Reference to Video](./examples/generate/create-omni-reference-to-video/) | `POST` | `/api/app/v1/generate/video/omni_reference_to_video` |
| [Text to Image](./examples/generate/create-text-to-image/) | `POST` | `/api/app/v1/generate/image/text_to_image` |
| [Text to Speech](./examples/generate/create-audio/) | `POST` | `/api/app/v1/generate/audio` |

### AI Avatar

| API | Method | Endpoint |
| --- | --- | --- |
| [Image Face Swap](./examples/ai-avatar/face-swap/) | `POST` | `/api/app/v1/process/image/face_swap` |
| [Image Head Swap](./examples/ai-avatar/head-swap/) | `POST` | `/api/app/v1/process/image/head_swap` |
| [Image & Audio Driven Video](./examples/ai-avatar/image-audio-driven-video/) | `POST` | `/api/app/v1/generate/video/image_audio_driven` |
| [Image Outfit Swap](./examples/ai-avatar/outfit-swap/) | `POST` | `/api/app/v1/process/image/outfit_swap` |
| [Video Character Replacement](./examples/ai-avatar/character-replacement/) | `POST` | `/api/app/v1/process/video/character_replacement` |
| [Video Head Swap](./examples/ai-avatar/video-head-swap/) | `POST` | `/api/app/v1/process/video/animate_head_swap` |
| [Video Face Swap Plus](./examples/ai-avatar/face-swap-plus/) | `POST` | `/api/app/v1/process/video/face_swap_plus` |
| [Video Character Replacement Plus](./examples/ai-avatar/character-replacement-plus/) | `POST` | `/api/app/v1/process/video/character_replacement_plus` |

### Process

| API | Method | Endpoint |
| --- | --- | --- |
| [Subtitle Removal](./examples/process/create-video-subtitle-removal/) | `POST` | `/api/app/v1/process/video/subtitle_removal` |
| [Background Removal](./examples/process/create-video-background-removal/) | `POST` | `/api/app/v1/process/video/background_removal` |
| [Background Removal](./examples/process/create-image-background-removal/) | `POST` | `/api/app/v1/process/image/background_removal` |

### Video

| API | Method | Endpoint |
| --- | --- | --- |
| [MV Director](./examples/video/mv-director/) | `POST` | `/api/app/v1/generate/video/mv_director` |
| [Text & Image to Video](./examples/video/text-image-to-video/) | `POST` | `/api/app/v1/generate/video/text_image_to_video` |
| [Video Upscale](./examples/video/video-upscale/) | `POST` | `/api/app/v1/process/video/video_upscale` |
| [Trim Video](./examples/video/trim-video/) | `POST` | `/api/app/v1/process/video/trim_video` |
| [Merge Video](./examples/video/merge-video/) | `POST` | `/api/app/v1/process/video/merge_video` |
| [Resize Video](./examples/video/resize-video/) | `POST` | `/api/app/v1/process/video/resize_video` |
| [Rotate Video](./examples/video/rotate-video/) | `POST` | `/api/app/v1/process/video/rotate_video` |
| [Flip Video](./examples/video/flip-video/) | `POST` | `/api/app/v1/process/video/flip_video` |
| [Change Video Speed](./examples/video/change-video-speed/) | `POST` | `/api/app/v1/process/video/change_video_speed` |
| [Adjust Video Volume](./examples/video/adjust-video-volume/) | `POST` | `/api/app/v1/process/video/adjust_video_volume` |
| [Add Audio to Video](./examples/video/add-audio-to-video/) | `POST` | `/api/app/v1/process/video/add_audio_to_video` |
| [Add Logo to Video](./examples/video/add-logo-to-video/) | `POST` | `/api/app/v1/process/video/add_logo_to_video` |
| [Video Face Swap](./examples/video/video-face-swap/) | `POST` | `/api/app/v1/process/video/face_swap` |
| [Watermark Removal](./examples/video/watermark-removal/) | `POST` | `/api/app/v1/process/video/watermark_removal` |
| [Logo Removal](./examples/video/video-logo-removal/) | `POST` | `/api/app/v1/process/video/video_logo_removal` |
| [Watermark Removal By Prompt](./examples/video/watermark-removal-by-prompt/) | `POST` | `/api/app/v1/process/video/watermark_removal_by_prompt` |
| [Split Video](./examples/video/split-video/) | `POST` | `/api/app/v1/process/video/split_video` |
| [Video Object Removal](./examples/video/remove-video-object/) | `POST` | `/api/app/v1/process/video/object_removal` |
| [Object Removal By Prompt](./examples/video/remove-video-object-by-prompt/) | `POST` | `/api/app/v1/process/video/object_removal_by_prompt` |

### Image

| API | Method | Endpoint |
| --- | --- | --- |
| [Text to Image Turbo](./examples/image/text-to-image-turbo/) | `POST` | `/api/app/v1/generate/image/text_to_image_turbo` |
| [Photo Repair](./examples/image/photo-repair/) | `POST` | `/api/app/v1/process/image/photo_repair` |
| [Image Edit Turbo](./examples/image/image-edit-turbo/) | `POST` | `/api/app/v1/generate/image/image_edit_turbo` |

### Voice & Audio

| API | Method | Endpoint |
| --- | --- | --- |
| [Trim Audio](./examples/voice-audio/trim-audio/) | `POST` | `/api/app/v1/process/audio/trim_audio` |
| [Merge Audio](./examples/voice-audio/merge-audio/) | `POST` | `/api/app/v1/process/audio/merge_audio` |
| [Reverse Audio](./examples/voice-audio/reverse-audio/) | `POST` | `/api/app/v1/process/audio/reverse_audio` |
| [Change Audio Speed](./examples/voice-audio/change-audio-speed/) | `POST` | `/api/app/v1/process/audio/change_audio_speed` |
| [Adjust Audio Volume](./examples/voice-audio/adjust-audio-volume/) | `POST` | `/api/app/v1/process/audio/adjust_audio_volume` |
| [Shift Audio Pitch](./examples/voice-audio/shift-audio-pitch/) | `POST` | `/api/app/v1/process/audio/shift_audio_pitch` |

### Get-Started

| API | Method | Endpoint |
| --- | --- | --- |
| [Create Upload URL](./examples/get-started/create-upload-url/) | `POST` | `/api/app/v1/upload_urls` |

### Infra

| API | Method | Endpoint |
| --- | --- | --- |
| [Create Asset](./examples/infra/create-asset/) | `POST` | `/api/app/v1/assets` |
| [List Assets](./examples/infra/list-assets/) | `GET` | `/api/app/v1/assets` |
| [List Results](./examples/infra/list-results/) | `GET` | `/api/app/v1/results` |
| [Get Task](./examples/infra/get-task/) | `GET` | `/api/app/v1/tasks/{task_id}` |
| [List Tasks](./examples/infra/list-tasks/) | `GET` | `/api/app/v1/tasks` |
| [Sync Task](./examples/infra/sync-task/) | `POST` | `/api/app/v1/tasks/{task_id}/sync` |

### Documents & PDF

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
