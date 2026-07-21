# How to Change an Outfit in an Image with Claude MCP and Medux

Use a simple natural-language request in Claude, let MCP connect to Medux, upload a person image and a clothing reference, then download the generated outfit-swap result.

## What this example does

Use a simple natural-language request in Claude, let MCP connect to Medux, upload a person image and a clothing reference, then download the generated outfit-swap result.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `MEDUX_PRESIGNED_UPLOAD_URL` |
| API endpoint | [See API reference](https://medux.io/api-reference/edit/outfit-swap) |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Using Medux, change the girl's outfit in girl.JPEG to match the clothing shown in clothes.PNG. Upload the files using a curl command.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `MEDUX_PRESIGNED_UPLOAD_URL`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/outfit_change_claude_mcp.html)
- [API reference](https://medux.io/api-reference/edit/outfit-swap)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
