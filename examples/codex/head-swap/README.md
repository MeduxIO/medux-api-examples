# How to Swap a Head in an Image with Codex MCP and Medux

This guide turns the screen-recorded workflow into a clean publish-ready tutorial. Codex reads the request, calls the Medux MCP tool, uploads two local images, runs the head-swap task, polls the result, and returns the final image.

## What this example does

This guide turns the screen-recorded workflow into a clean publish-ready tutorial. Codex reads the request, calls the Medux MCP tool, uploads two local images, runs the head-swap task, polls the result, and returns the final image.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `head_swap` |
| API endpoint | [See API reference](https://medux.io/api-reference/edit/head-swap) |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Swap the head in "swap_head_src.jpg" with the head in "swap_head_target.jpg". Use medux. head swap!
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `head_swap`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/head_swap_codex_mcp.html)
- [API reference](https://medux.io/api-reference/edit/head-swap)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
