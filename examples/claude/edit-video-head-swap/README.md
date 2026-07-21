# How to Video Head Swap with Claude MCP and Medux

Learn how to use Claude MCP and Medux to animate a swapped face image with a driving video to produce a head swap video, including setup, request fields,…

## What this example does

Animate a swapped face image with a driving video to produce a head swap video.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_animate_head_swap` |
| API endpoint | `POST /api/app/v1/process/video/animate_head_swap` |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Animate a swapped face image with a driving video to produce a head swap video.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `face_image_file_id` | `string` | Required | Face reference image file id used for the head swap target. |
| `input_video_file_id` | `string` | Required | Driving video file id. |
| `width` | `integer` | Optional | Target output width. Default: 480. |
| `height` | `integer` | Optional | Target output height. Default: 832. |
| `positive_prompt` | `string` | Optional | Positive prompt text for the animation workflow. Default: 一个角色在说话. |
| `negative_prompt` | `string` | Optional | Negative prompt text. |
| `edit_prompt` | `string` | Optional | Edit instruction for preserving the swapped face identity. Default: 人脸保持不变. |
| `model_id` | `string` | Optional | Animate head swap model id. Default: animate-head-swap-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_animate_head_swap`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/edit_video_head_swap_claude_mcp.html)
- [API reference](https://medux.io/api-reference/edit/video-head-swap)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
