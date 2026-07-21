# How to Create Avatar by Image with Codex MCP and Medux

Learn how to use Codex MCP and Medux to create a reusable avatar asset from an uploaded image file, including setup, request fields, tool approval, and…

## What this example does

Create a reusable avatar asset from an uploaded image file.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_avatar_clone_by_image` |
| API endpoint | `POST /api/app/v1/clone/avatar/by_image` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Clone a reusable avatar from the uploaded portrait image {file id}. Title it Official avatar image clone sample.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `file_id` | `string` | Required | Provide the value described in the API reference. |
| `title` | `string` | Optional | Provide the value described in the API reference. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_avatar_clone_by_image`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/clone_create_avatar_by_image_codex_mcp.html)
- [API reference](https://medux.io/api-reference/clone/create-avatar-by-image)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
