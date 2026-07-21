# How to Create Asset with Codex MCP and Medux

Learn how to use Codex MCP and Medux to create an asset record from a file that was uploaded through a direct upload url, including setup, request fields,…

## What this example does

Create an asset record from a file that was uploaded through a direct upload URL.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_create_asset` |
| API endpoint | `POST /api/app/v1/assets` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Use Medux to run Create Asset. Review the required inputs, call medux_create_asset, wait for the result if a task is returned, and report the output clearly.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `category` | `string` | Optional | Asset category, used for validation and later rendering. Allowed values: - CATEGORY UNDEFINED - Not specified. - MEDIA - Uploaded source media. - AVATAR - Reusable avatar asset. - VOICE - Reusable voice asset. |
| `file_size_bytes` | `int64` | Optional | Original file size, in bytes. |
| `name` | `string` | Optional | Display name provided by the user. This value may be empty. |
| `storage_object.key` | `string` | Optional | Provide the value described in the API reference. |
| `storage_object.url` | `string` | Optional | Provide the value described in the API reference. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_create_asset`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/infra_create_asset_codex_mcp.html)
- [API reference](https://medux.io/api-reference/infra/create-asset)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
