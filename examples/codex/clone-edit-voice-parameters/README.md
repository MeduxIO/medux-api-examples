# How to Edit Voice Parameters with Codex MCP and Medux

Learn how to use Codex MCP and Medux to update tuning parameters for an existing reusable voice asset, including setup, request fields, tool approval, and…

## What this example does

Update tuning parameters for an existing reusable voice asset.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_edit_voice_parameters` |
| API endpoint | `POST /api/app/v1/clone/voice/{voice_asset_id}/parameters` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Use Medux to run Edit Voice Parameters. Review the required inputs, call medux_edit_voice_parameters, wait for the result if a task is returned, and report the output clearly.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `voice_asset_id` | `string` | Required | Provide the value described in the API reference. |
| `emotion` | `int32` | Optional | Provide the value described in the API reference. |
| `speed` | `int32` | Optional | Provide the value described in the API reference. |
| `title` | `string` | Optional | Provide the value described in the API reference. |
| `tone` | `int32` | Optional | Provide the value described in the API reference. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_edit_voice_parameters`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/clone_edit_voice_parameters_codex_mcp.html)
- [API reference](https://medux.io/api-reference/clone/edit-voice-parameters)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
