# How to Image Face Swap with Codex MCP and Medux

Learn how to use Codex MCP and Medux to swap a face from one image onto another while keeping the target pose and lighting, including setup, request fields,…

## What this example does

Swap a face from one image onto another while keeping the target pose and lighting.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_image_face_swap` |
| API endpoint | `POST /api/app/v1/process/image/face_swap` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Swap a face from one image onto another while keeping the target pose and lighting.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `source_image_file_id` | `string` | Required | Source image file id. |
| `target_face_image_file_id` | `string` | Required | Target face image file id. |
| `model_id` | `string` | Optional | Face swap model id. Default: image-face-swap-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_image_face_swap`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/edit_face_swap_codex_mcp.html)
- [API reference](https://medux.io/api-reference/edit/face-swap)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
