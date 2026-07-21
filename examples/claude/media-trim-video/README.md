# How to Trim Video with Claude MCP and Medux

Learn how to use Claude MCP and Medux to cut a video to a specified time range, including setup, request fields, tool approval, and results.

## What this example does

Cut a video to a specified time range.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_trim_video` |
| API endpoint | `POST /api/app/v1/process/video/trim_video` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Cut a video to a specified time range.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_file_id` | `string` | Required | Input video file id. |
| `start_time` | `string` | Optional | e.g. 00:00:05 |
| `end_time` | `string` | Optional | e.g. 00:00:30 |
| `duration` | `string` | Optional | e.g. 00:00:25. At least one of start time/end time/duration required. |
| `model_id` | `string` | Optional | Model Default: trim-video-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_trim_video`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/media_trim_video_claude_mcp.html)
- [API reference](https://medux.io/api-reference/media/trim-video)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
