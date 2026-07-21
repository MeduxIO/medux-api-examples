# How to Create Audio with Claude MCP and Medux

Learn how to use Claude MCP and Medux to generate speech audio from text using a reusable voice asset, including setup, request fields, tool approval, and…

## What this example does

Generate speech audio from text using a reusable voice asset.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_speech_create_audio` |
| API endpoint | `POST /api/app/v1/generate/audio` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Generate speech audio from this text using voice asset id {voice asset id} and model id speech-standard.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `links` | `array<string>` | Optional | Optional reference links submitted from the Playground form. |
| `model` | `string` | Optional | Generation model label or version selected in the Playground form. |
| `model_id` | `string` | Optional | Stable public Medux model identifier. |
| `text` | `string` | Optional | Provide the value described in the API reference. |
| `title` | `string` | Optional | Provide the value described in the API reference. |
| `voice_asset_id` | `string` | Required | Reusable voice asset used for text-to-speech generation. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_speech_create_audio`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/generate_create_audio_claude_mcp.html)
- [API reference](https://medux.io/api-reference/generate/create-audio)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
