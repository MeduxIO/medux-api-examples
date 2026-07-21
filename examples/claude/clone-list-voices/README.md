# How to List Voices with Claude MCP and Medux

Learn how to use Claude MCP and Medux to list reusable voice assets owned by the authenticated user, including setup, request fields, tool approval, and…

## What this example does

List reusable voice assets owned by the authenticated user.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_list_voices` |
| API endpoint | `GET /api/app/v1/clone/voices` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Use Medux to run List Voices. Review the required inputs, call medux_list_voices, wait for the result if a task is returned, and report the output clearly.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `cursor` | `string` | Optional | Provide the value described in the API reference. |
| `limit` | `int32` | Optional | Provide the value described in the API reference. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_list_voices`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/clone_list_voices_claude_mcp.html)
- [API reference](https://medux.io/api-reference/clone/list-voices)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
