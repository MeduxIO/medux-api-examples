# How to Adjust Audio Pitch with Claude MCP and Medux

Use one natural-language request to create both a higher-pitched and lower-pitched version of an audio file. Claude handles the workflow through MCP, while Medux performs the media processing.

## What this example does

Use one natural-language request to create both a higher-pitched and lower-pitched version of an audio file. Claude handles the workflow through MCP, while Medux performs the media processing.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `adjust_audio_pitch` |
| API endpoint | [See API reference](https://medux.io/api-reference/media/shift-audio-pitch) |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
project/ └── sample-audio.m4a
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `adjust_audio_pitch`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/adjust_audio_pitch_claude_mcp.html)
- [API reference](https://medux.io/api-reference/media/shift-audio-pitch)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
