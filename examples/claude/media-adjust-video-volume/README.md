# How to Adjust Video Volume with Claude MCP and Medux

Learn how to use Claude MCP and Medux to adjust the audio volume of a video, including setup, request fields, tool approval, and results.

## What this example does

Adjust the audio volume of a video.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_adjust_video_volume` |
| API endpoint | `POST /api/app/v1/process/video/adjust_video_volume` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Adjust the audio volume of a video.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_file_id` | `string` | Required | Input video file id. |
| `volume` | `string` | Required | ffmpeg volume expression e.g. 1.5, 0.8, 2dB. |
| `model_id` | `string` | Optional | Model Default: adjust-video-volume-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_adjust_video_volume`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/media_adjust_video_volume_claude_mcp.html)
- [API reference](https://medux.io/api-reference/media/adjust-video-volume)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
