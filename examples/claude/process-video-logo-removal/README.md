# How to Create Video Logo Removal with Claude MCP and Medux

Learn how to use Claude MCP and Medux to remove a logo from a video using an optional logo reference and motion mode, including setup, request fields, tool…

## What this example does

Remove a logo from a video using an optional logo reference and motion mode.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_video_logo_removal` |
| API endpoint | `POST /api/app/v1/process/video/video_logo_removal` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Remove a logo from a video using an optional logo reference and motion mode.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `input_video_file_id` | `string` | Required | Input video file id. |
| `logo_file_id` | `string` | Optional | Optional logo image file id used to build the logo mask session. |
| `video_size` | `object` | Optional | Optional original video size hint as [width, height]. |
| `logo_type` | `string` | Optional | Logo motion mode for mask generation. Default: moving. Default: moving. |
| `model_id` | `string` | Optional | Video logo removal model id. Default: video-logo-removal-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_video_logo_removal`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/process_video_logo_removal_claude_mcp.html)
- [API reference](https://medux.io/api-reference/process/video-logo-removal)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
