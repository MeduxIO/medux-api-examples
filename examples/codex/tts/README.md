# How to Clone a Voice and Generate Speech with Codex MCP and Medux

This tutorial shows how to provide a reference voice file and a text file, then let Codex call Medux through MCP to upload the audio, create a voice clone, synthesize speech, and save the generated WAV file locally.

## What this example does

This tutorial shows how to provide a reference voice file and a text file, then let Codex call Medux through MCP to upload the audio, create a voice clone, synthesize speech, and save the generated WAV file locally.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_file_create_upload_url` |
| API endpoint | [See API reference](https://medux.io/api-reference/clone/create-voice) |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
/Users/chuan/projects/test_mudex/ ├── reference_voice.wav # Reference voice used for cloning ├── tts.txt # Text to synthesize └── config/
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_file_create_upload_url`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/tts_codex_mcp.html)
- [API reference](https://medux.io/api-reference/clone/create-voice)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
