# How to Create Image to Video with Codex MCP and Medux

Learn how to use Codex MCP and Medux to generate a video from a source image and text prompt, including setup, request fields, tool approval, and results.

## What this example does

Generate a video from a source image and text prompt.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_video_generate_image_to_video` |
| API endpoint | `POST /api/app/v1/generate/video/image_to_video` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Generate a 5 second 720P 16:9 video from uploaded image {file id} and this motion prompt using model id wan-2-6-image-to-video. This model requires Starter or higher.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `aspect_ratio` | `string` | Optional | Requested output aspect ratio, for example 16:9 or 9:16. |
| `clarity` | `string` | Optional | Requested output clarity, for example 720P or 1080P. |
| `duration_seconds` | `int32` | Optional | Requested output duration in seconds. |
| `file_id` | `string` | Optional | Provide the value described in the API reference. |
| `model_id` | `string` | Optional | Stable public Medux model identifier. |
| `prompt` | `string` | Optional | Provide the value described in the API reference. |
| `title` | `string` | Optional | Provide the value described in the API reference. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_video_generate_image_to_video`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/generate_create_image_to_video_codex_mcp.html)
- [API reference](https://medux.io/api-reference/generate/create-image-to-video)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
