# How to Replace a Video Character with Claude MCP and Medux

Use Claude as the operator and Medux as the media engine. In one guided workflow, Claude prepares the assets, uploads them, starts the character-replacement job, monitors progress, and returns the finished video.

## What this example does

Use Claude as the operator and Medux as the media engine. In one guided workflow, Claude prepares the assets, uploads them, starts the character-replacement job, monitors progress, and returns the finished video.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_file_create_upload_url` |
| API endpoint | [See API reference](https://medux.io/api-reference/edit/character-replacement) |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Example project folder/Users/your-name/projects/medux-character-replacement/ ├── character.mp4 └── character.jpg
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_file_create_upload_url`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/character_replacement_claude_mcp.html)
- [API reference](https://medux.io/api-reference/edit/character-replacement)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
