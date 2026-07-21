# How to Create a Lip-Synced Avatar Video with Codex MCP and Medux

This guide turns the operation video into a clean, publish-ready workflow: prepare a source avatar video and an audio track, let Codex call Medux through MCP, then download a polished MP4 where the mouth, lips, and tongue follow the speech.

## What this example does

This guide turns the operation video into a clean, publish-ready workflow: prepare a source avatar video and an audio track, let Codex call Medux through MCP, then download a polished MP4 where the mouth, lips, and tongue follow the speech.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `MEDUX_API_KEY` |
| API endpoint | [See API reference](https://medux.io/api-reference/generate/create-audio-driven-video) |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
# Example project layout project/ avatar.mp4 reference_voice.wav tts.txt config/ output/
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `MEDUX_API_KEY`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/lipsync_codex_mcp.html)
- [API reference](https://medux.io/api-reference/generate/create-audio-driven-video)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
