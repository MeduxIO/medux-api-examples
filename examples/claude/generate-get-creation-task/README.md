# How to Get Creation Task with Claude MCP and Medux

Learn how to use Claude MCP and Medux to return the current state of a media generation task, including setup, request fields, tool approval, and results.

## What this example does

Return the current state of a media generation task.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_get_creation_task` |
| API endpoint | `GET /api/app/v1/generate/tasks/{task_id}` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Use Medux to run Get Creation Task. Review the required inputs, call medux_get_creation_task, wait for the result if a task is returned, and report the output clearly.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `task_id` | `string` | Required | Provide the value described in the API reference. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_get_creation_task`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/generate_get_creation_task_claude_mcp.html)
- [API reference](https://medux.io/api-reference/generate/get-creation-task)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
