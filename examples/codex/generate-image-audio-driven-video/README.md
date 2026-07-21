# How to Create Image Audio Driven Video with Codex MCP and Medux

Learn how to use Codex MCP and Medux to generate a talking video from a reference image, driving audio, and prompt text, including setup, request fields,…

## What this example does

Generate a talking video from a reference image, driving audio, and prompt text.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_image_audio_driven_video` |
| API endpoint | `POST /api/app/v1/generate/video/image_audio_driven` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Generate a talking video from a reference image, driving audio, and prompt text.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `prompt_text` | `string` | Required | Talking prompt text used to guide video generation. |
| `prompt_image_file_id` | `string` | Required | Reference image file id. |
| `prompt_audio_file_id` | `string` | Required | Driving audio file id. |
| `resolution` | `string` | Optional | Prompt image or prompt video frame resize target before generation. Default: 720p. |
| `model_id` | `string` | Optional | Image audio driven video model id. Default: image-audio-driven-video-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_image_audio_driven_video`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/generate_image_audio_driven_video_codex_mcp.html)
- [API reference](https://medux.io/api-reference/generate/image-audio-driven-video)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
