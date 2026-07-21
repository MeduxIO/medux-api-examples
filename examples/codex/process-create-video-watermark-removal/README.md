# How to Create Video Watermark Removal with Codex MCP and Medux

Learn how to use Codex MCP and Medux to create a video processing task that removes a watermark from an uploaded video, including setup, request fields,…

## What this example does

Create a video processing task that removes a watermark from an uploaded video.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_video_remove_watermark` |
| API endpoint | `POST /api/app/v1/process/video/watermark_removal` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Remove the watermark from the uploaded source video {file id}. If the watermark area is known, pass region {x, y, width, height}.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `file_id` | `string` | Required | Provide the value described in the API reference. |
| `region.height` | `int32` | Optional | Provide the value described in the API reference. |
| `region.width` | `int32` | Optional | Provide the value described in the API reference. |
| `region.x` | `int32` | Optional | X coordinate of the region's top-left corner in pixels. |
| `region.y` | `int32` | Optional | Y coordinate of the region's top-left corner in pixels. |
| `title` | `string` | Optional | Provide the value described in the API reference. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_video_remove_watermark`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/process_create_video_watermark_removal_codex_mcp.html)
- [API reference](https://medux.io/api-reference/process/create-video-watermark-removal)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
