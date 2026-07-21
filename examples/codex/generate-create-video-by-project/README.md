# How to Create Video by Project with Codex MCP and Medux

Learn how to use Codex MCP and Medux to start video generation from an existing flyworks provider project, including setup, request fields, tool approval,…

## What this example does

Start video generation from an existing Flyworks provider project.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_create_video_by_project` |
| API endpoint | `POST /api/app/v1/generate/video/by_project` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Use Medux to run Create Video by Project. Review the required inputs, call medux_create_video_by_project, wait for the result if a task is returned, and report the output clearly.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `project_id` | `string` | Optional | Provide the value described in the API reference. |
| `title` | `string` | Optional | Provide the value described in the API reference. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_create_video_by_project`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/generate_create_video_by_project_codex_mcp.html)
- [API reference](https://medux.io/api-reference/generate/create-video-by-project)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
