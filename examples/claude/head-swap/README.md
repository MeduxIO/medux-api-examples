# How to Swap a Head in an Image with Claude MCP and Medux

Use one natural-language request in Claude to upload a source head and a target image, call the Medux head-swap workflow through MCP, monitor the task, and save the generated result.

## What this example does

Use one natural-language request in Claude to upload a source head and a target image, call the Medux head-swap workflow through MCP, monitor the task, and save the generated result.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `head_swap` |
| API endpoint | [See API reference](https://medux.io/api-reference/edit/head-swap) |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Swap the head in "swap_head_src.jpg" with the head in "swap_head_target.jpg". Use Medux through MCP, upload the files with curl, run the head-swap task, and save the result in the current project folder.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `head_swap`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/head_swap_claude_mcp.html)
- [API reference](https://medux.io/api-reference/edit/head-swap)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
