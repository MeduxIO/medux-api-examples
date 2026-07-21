# How to Flip Video with Codex MCP and Medux

Learn how to use Codex MCP and Medux to flip a video horizontally, vertically, or both, including setup, request fields, tool approval, and results.

## What this example does

Flip a video horizontally, vertically, or both.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_flip_video` |
| API endpoint | `POST /api/app/v1/process/video/flip_video` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Flip a video horizontally, vertically, or both.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_file_id` | `string` | Required | Input video file id. |
| `flip_mode` | `string` | Required | Flip direction. |
| `model_id` | `string` | Optional | Model Default: flip-video-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_flip_video`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/media_flip_video_codex_mcp.html)
- [API reference](https://medux.io/api-reference/media/flip-video)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
