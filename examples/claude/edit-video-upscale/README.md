# How to Video Upscale with Claude MCP and Medux

Learn how to use Claude MCP and Medux to upscale a video to a higher resolution, including setup, request fields, tool approval, and results.

## What this example does

Upscale a video to a higher resolution.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_video_upscale` |
| API endpoint | `POST /api/app/v1/process/video/video_upscale` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Upscale a video to a higher resolution.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_file_id` | `string` | Required | Input video file id. |
| `new_resolution` | `integer` | Optional | Target maximum side length after upscale, e.g. 2160. Default: 2160. |
| `model_id` | `string` | Optional | Video upscale model id. Default: video-upscale-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_video_upscale`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/edit_video_upscale_claude_mcp.html)
- [API reference](https://medux.io/api-reference/edit/video-upscale)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
