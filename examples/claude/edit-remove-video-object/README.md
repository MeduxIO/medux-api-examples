# How to Remove Video Object with Claude MCP and Medux

Learn how to use Claude MCP and Medux to remove an object from a video by mask regions, including setup, request fields, tool approval, and results.

## What this example does

Remove an object from a video by mask regions.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_remove_video_object` |
| API endpoint | `POST /api/app/v1/process/video/remove_video_object` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Remove an object from a video by mask regions.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_file_id` | `string` | Required | Input video file id. |
| `mask_regions` | `object` | Required | Regions to remove, e.g. [[x, y, width, height]]. |
| `model_id` | `string` | Optional | Model Default: remove-video-object-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_remove_video_object`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/edit_remove_video_object_claude_mcp.html)
- [API reference](https://medux.io/api-reference/edit/remove-video-object)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
