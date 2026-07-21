# How to Create Upload URL with Claude MCP and Medux

Learn how to use Claude MCP and Medux to create a pre-signed upload url and file reference for a direct client upload, including setup, request fields, tool…

## What this example does

Create a pre-signed upload URL and file reference for a direct client upload.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_create_upload_url` |
| API endpoint | `POST /api/app/v1/upload_urls` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Use Medux to run Create Upload URL. Review the required inputs, call medux_create_upload_url, wait for the result if a task is returned, and report the output clearly.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `extension` | `string` | Optional | File extension without a leading dot, such as mp4. |
| `media_type` | `string` | Optional | Media type used to validate extension and build the object path. Allowed values: - MEDIA TYPE UNDEFINED - Not specified. - VIDEO - Video file, such as mp4. - AUDIO - Audio file, such as mp3. - IMAGE - Image file, such… |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_create_upload_url`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/get_started_create_upload_url_claude_mcp.html)
- [API reference](https://medux.io/api-reference/get-started/create-upload-url)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
