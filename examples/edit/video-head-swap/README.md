# Video Head Swap

Animate a swapped face image with a driving video to produce a head swap video.

## Endpoint

```http
POST /api/app/v1/process/video/animate_head_swap
```

Base URL: `https://api.medux.io`

Animate a swapped face image with a driving video to produce a head swap video.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Upload the source file and create a file reference before calling this endpoint.
- Successful requests return a Medux task record immediately. Use the task query or sync endpoints to track completion.
- All file inputs must be uploaded and persisted as file references before submission.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `face_image_file_id` | `string` | Required | `BODY` | Face reference image file_id used for the head swap target. |
| `input_video_file_id` | `string` | Required | `BODY` | Driving video file_id. |
| `width` | `integer` | Optional | `BODY` | Target output width. Default: 480. |
| `height` | `integer` | Optional | `BODY` | Target output height. Default: 832. |
| `positive_prompt` | `string` | Optional | `BODY` | Positive prompt text for the animation workflow. Default: 一个角色在说话. |
| `negative_prompt` | `string` | Optional | `BODY` | Negative prompt text. |
| `edit_prompt` | `string` | Optional | `BODY` | Edit instruction for preserving the swapped face identity. Default: 人脸保持不变. |
| `model_id` | `string` | Optional | `BODY` | Animate head swap model id. Default: animate-head-swap-default. |
| `title` | `string` | Optional | `BODY` | Optional task title. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `FILE_ID` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/process/video/animate_head_swap \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"edit_prompt":"人脸保持不变","face_image_file_id":"FILE_ID","height":832,"input_video_file_id":"FILE_ID","model_id":"animate-head-swap-default","positive_prompt":"一个角色在说话","width":480}'
```

The same command is available in [`curl.sh`](./curl.sh).

The curl form mirrors the official reference. Replace uppercase placeholders such as `FILE_ID`, `TASK_ID`, or `MODEL_ID` inline before running it; the Python and JavaScript examples resolve their documented placeholders from environment variables.

## Python

Install the dependency and run:

```bash
python3 -m pip install -r ../../../requirements.txt
python3 example.py
```

See [`example.py`](./example.py).

## JavaScript

Node.js 18 or newer is required:

```bash
node example.mjs
```

See [`example.mjs`](./example.mjs).

## Response

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `code` | `int32` | Optional | `RESPONSE` | Application response code.<br><br>\| Code \| Meaning \|<br>\| ---- \| ------- \|<br>\| `0` \| OK \|<br>\| `12` \| Invalid input \|<br>\| `1401` \| Insufficient credits \|<br>\| `1404` \| Provider returned an error \|<br>\| `1405` \| Provider request timed out \|<br>\| `13` \| Authentication is required \|<br>\| `16` \| Rate limit exceeded \|<br>\| `99` \| Server error \|<br>Options: `0`, `12`, `1410`, `1409`, `1401`, `1404`, `1405`, `13`, `16`, `99` |
| `data.asset` | `object` | Optional | `RESPONSE` | Asset created or returned by the operation when available. |
| `data.paid_plan_required` | `object` | Optional | `RESPONSE` | Paid-plan requirement details when the selected capability is unavailable on the current plan. |
| `data.task` | `object` | Optional | `RESPONSE` | Task record created or returned by an asynchronous operation. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error` |

### Response handling

This response can include `data.task`. Persist the returned task ID and use the [relevant task-status endpoint](../../process/get-process-task/) until the task reaches a terminal state. Do not treat HTTP 200 alone as proof that asynchronous media processing has completed.

Application response codes and meanings are reproduced in the response-field table above from the official reference. Handle the documented non-success messages explicitly: `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error`.

## Official sample

No official media sample is currently documented for this endpoint.

## MCP alternative

The same capability is optionally available through Medux MCP.

- MCP endpoint: `https://mcp.medux.io/api/mcp/v1`
- Tool: `medux_animate_head_swap`
- Result type: `—`


## Related APIs

- [Sync Task](../../infra/sync-task/) — Refresh task state from the upstream provider.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/edit/video-head-swap)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
