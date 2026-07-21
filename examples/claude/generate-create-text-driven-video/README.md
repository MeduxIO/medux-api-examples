# How to Create Text Driven Video with Claude MCP and Medux

Learn how to use Claude MCP and Medux to generate an avatar video from text using a reusable avatar and voice, including setup, request fields, tool…

## What this example does

Generate an avatar video from text using a reusable avatar and voice.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_video_create_text_driven` |
| API endpoint | `POST /api/app/v1/generate/video/text_driven` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Create a 7 second 1080P 16:9 talking video from this script using avatar asset id {avatar asset id}, voice asset id {voice asset id}, and model id talking-video-text-standard.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `aspect_ratio` | `string` | Optional | Requested output aspect ratio, such as 16:9 or 9:16. |
| `avatar_asset_id` | `string` | Required | Reusable avatar asset ID owned by the current user or listed as an official public asset. |
| `clarity` | `string` | Optional | Requested output resolution label, such as 1080P or 2K. |
| `duration_seconds` | `int32` | Optional | Requested output duration, in seconds. |
| `links` | `array<string>` | Optional | Optional reference links submitted from the Playground form. |
| `model` | `string` | Optional | Generation model label or version selected in the Playground form. |
| `model_id` | `string` | Optional | Stable public Medux model identifier. |
| `text` | `string` | Optional | Provide the value described in the API reference. |
| `title` | `string` | Optional | Provide the value described in the API reference. |
| `voice_asset_id` | `string` | Required | Reusable voice asset used for text-driven lip sync. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_video_create_text_driven`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/generate_create_text_driven_video_claude_mcp.html)
- [API reference](https://medux.io/api-reference/generate/create-text-driven-video)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
