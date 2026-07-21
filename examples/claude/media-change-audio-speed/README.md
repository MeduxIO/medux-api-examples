# How to Change Audio Speed with Claude MCP and Medux

Learn how to use Claude MCP and Medux to speed up or slow down an audio file, including setup, request fields, tool approval, and results.

## What this example does

Speed up or slow down an audio file.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_change_audio_speed` |
| API endpoint | `POST /api/app/v1/process/audio/change_audio_speed` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Speed up or slow down an audio file.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_file_id` | `string` | Required | Input audio file id. |
| `speed` | `number` | Required | Positive float, e.g. 1.5 for 1.5x speed. |
| `model_id` | `string` | Optional | Model Default: change-audio-speed-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_change_audio_speed`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/media_change_audio_speed_claude_mcp.html)
- [API reference](https://medux.io/api-reference/media/change-audio-speed)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
