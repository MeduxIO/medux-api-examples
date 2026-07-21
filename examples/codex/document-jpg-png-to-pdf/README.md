# How to JPG/PNG to PDF with Codex MCP and Medux

Learn how to use Codex MCP and Medux to convert jpg or png images into a pdf, including setup, request fields, tool approval, and results.

## What this example does

Convert JPG or PNG images into a PDF.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_jpg_png_to_pdf` |
| API endpoint | `POST /api/app/v1/process/asset/jpg_png_to_pdf` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Convert JPG or PNG images into a PDF.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_file_ids` | `array<string>` | Required | Input JPG/PNG file id list. |
| `model_id` | `string` | Optional | Model Default: jpg-png-to-pdf-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_jpg_png_to_pdf`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/document_jpg_png_to_pdf_codex_mcp.html)
- [API reference](https://medux.io/api-reference/document/jpg-png-to-pdf)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
