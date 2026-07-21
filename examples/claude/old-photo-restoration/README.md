# How to Restore Old Photos with Claude MCP and Medux

Use a single natural-language request to let Claude upload an old photo, call the right Medux restoration workflow through MCP, monitor the task, and save the enhanced result locally.

## What this example does

Use a single natural-language request to let Claude upload an old photo, call the right Medux restoration workflow through MCP, monitor the task, and save the enhanced result locally.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `old_photo_restoration` |
| API endpoint | [See API reference](https://medux.io/api-reference/edit/photo-repair) |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Restore Old Photo [your-photo.jpg]. Upload the file using a curl command.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `old_photo_restoration`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/old_photo_restoration_claude_mcp.html)
- [API reference](https://medux.io/api-reference/edit/photo-repair)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
