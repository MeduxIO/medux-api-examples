# How to PPT to PDF with Claude MCP and Medux

Learn how to use Claude MCP and Medux to convert a powerpoint (.pptx) file to pdf, including setup, request fields, tool approval, and results.

## What this example does

Convert a PowerPoint (.pptx) file to PDF.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_ppt_to_pdf` |
| API endpoint | `POST /api/app/v1/process/asset/ppt_to_pdf` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Convert a PowerPoint (.pptx) file to PDF.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_file_id` | `string` | Required | Input PowerPoint file id. |
| `model_id` | `string` | Optional | Model Default: ppt-to-pdf-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_ppt_to_pdf`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/document_ppt_to_pdf_claude_mcp.html)
- [API reference](https://medux.io/api-reference/document/ppt-to-pdf)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
