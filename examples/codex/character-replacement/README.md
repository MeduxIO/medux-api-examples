# How to Replace a Video Character with Codex MCP and Medux

This tutorial shows a compact Codex + MCP workflow: upload a source video and a reference character image, call the Medux character replacement tool, wait for the render, and save the finished MP4.

## What this example does

This tutorial shows a compact Codex + MCP workflow: upload a source video and a reference character image, call the Medux character replacement tool, wait for the render, and save the finished MP4.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `MEDUX_PRESIGNED_UPLOAD_URL` |
| API endpoint | [See API reference](https://medux.io/api-reference/edit/character-replacement) |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
project/ ├── character.mp4 # source video with the original person └── character.jpg # reference character image for replacement
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `MEDUX_PRESIGNED_UPLOAD_URL`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/character_replacement_codex_mcp.html)
- [API reference](https://medux.io/api-reference/edit/character-replacement)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
