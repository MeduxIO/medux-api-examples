# How to PDF to Images with Claude MCP and Medux

Learn how to use Claude MCP and Medux to convert pdf pages to images (zip output), including setup, request fields, tool approval, and results.

## What this example does

Convert PDF pages to images (zip output).

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_pdf_to_images` |
| API endpoint | `POST /api/app/v1/process/asset/pdf_to_images` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Convert PDF pages to images (zip output).
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_file_id` | `string` | Required | Input PDF file id. |
| `image_format` | `string` | Optional | Output image format. Default: jpeg. |
| `model_id` | `string` | Optional | Model Default: pdf-to-images-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_pdf_to_images`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/document_pdf_to_images_claude_mcp.html)
- [API reference](https://medux.io/api-reference/document/pdf-to-images)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
