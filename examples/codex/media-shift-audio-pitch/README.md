# How to Shift Audio Pitch with Codex MCP and Medux

Learn how to use Codex MCP and Medux to shift the pitch of an audio file, including setup, request fields, tool approval, and results.

## What this example does

Shift the pitch of an audio file.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_shift_audio_pitch` |
| API endpoint | `POST /api/app/v1/process/audio/shift_audio_pitch` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Shift the pitch of an audio file.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_file_id` | `string` | Required | Input audio file id. |
| `semitones` | `number` | Required | Pitch shift amount in semitones. |
| `sample_rate` | `integer` | Optional | Output sample rate, default 44100. Default: 44100. |
| `model_id` | `string` | Optional | Model Default: shift-audio-pitch-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_shift_audio_pitch`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/media_shift_audio_pitch_codex_mcp.html)
- [API reference](https://medux.io/api-reference/media/shift-audio-pitch)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
