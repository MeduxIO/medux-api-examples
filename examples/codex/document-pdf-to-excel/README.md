# How to PDF to Excel with Codex MCP and Medux

Learn how to use Codex MCP and Medux to extract tables from a pdf into an excel (.xlsx) file, including setup, request fields, tool approval, and results.

## What this example does

Extract tables from a PDF into an Excel (.xlsx) file.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_pdf_to_excel` |
| API endpoint | `POST /api/app/v1/process/asset/pdf_to_excel` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Extract tables from a PDF into an Excel (.xlsx) file.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_file_id` | `string` | Required | Input PDF file id. |
| `pages` | `string` | Optional | Pages to extract, default all. Default: all. |
| `flavor` | `string` | Optional | Extraction method. Default: stream. |
| `model_id` | `string` | Optional | Model Default: pdf-to-excel-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_pdf_to_excel`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/document_pdf_to_excel_codex_mcp.html)
- [API reference](https://medux.io/api-reference/document/pdf-to-excel)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
