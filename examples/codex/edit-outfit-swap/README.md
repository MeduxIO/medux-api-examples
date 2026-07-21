# How to Image Outfit Swap with Codex MCP and Medux

Learn how to use Codex MCP and Medux to transfer the outfit from the reference image onto the target subject, including setup, request fields, tool…

## What this example does

Transfer the outfit from the reference image onto the target subject.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_image_outfit_swap` |
| API endpoint | `POST /api/app/v1/process/image/outfit_swap` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Transfer the outfit from the reference image onto the target subject.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `source_image_file_id` | `string` | Required | Source image file id. |
| `target_outfit_image_file_id` | `string` | Required | Target outfit image file id. |
| `model_id` | `string` | Optional | Outfit swap model id. Default: image-outfit-swap-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_image_outfit_swap`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/edit_outfit_swap_codex_mcp.html)
- [API reference](https://medux.io/api-reference/edit/outfit-swap)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
