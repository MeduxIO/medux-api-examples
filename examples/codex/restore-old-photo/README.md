# How to Restore Old Photos with Codex MCP and Medux

This tutorial shows a clean agent workflow: Codex finds the local old photo, calls the Medux photo-repair tool through MCP, uploads the image, tracks the task, and saves the restored PNG back into the workspace.

## What this example does

This tutorial shows a clean agent workflow: Codex finds the local old photo, calls the Medux photo-repair tool through MCP, uploads the image, tracks the task, and saves the restored PNG back into the workspace.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `MEDUX_FILE_URL` |
| API endpoint | [See API reference](https://medux.io/api-reference/edit/photo-repair) |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
User prompt: Using medux to restore Old Photo (repair.jpeg).
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `MEDUX_FILE_URL`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/restore_old_photo_codex_mcp.html)
- [API reference](https://medux.io/api-reference/edit/photo-repair)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
