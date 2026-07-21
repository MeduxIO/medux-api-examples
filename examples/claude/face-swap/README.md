# How to Swap Faces in an Image with Claude MCP and Medux

Use a single natural-language request in Claude, let MCP connect to Medux, upload two images, run the face-swap task, and save the generated result locally.

## What this example does

Use a single natural-language request in Claude, let MCP connect to Medux, upload two images, run the face-swap task, and save the generated result locally.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `MEDUX_RESULT_URL` |
| API endpoint | [See API reference](https://medux.io/api-reference/edit/face-swap) |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
swap_face_src.jpg
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `MEDUX_RESULT_URL`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/face_swap_claude_mcp.html)
- [API reference](https://medux.io/api-reference/edit/face-swap)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
