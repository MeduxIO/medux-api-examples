# Create Video Logo Removal

Remove a logo from a video using an optional logo reference and motion mode.

## Endpoint

```http
POST /api/app/v1/process/video/video_logo_removal
```

Base URL: `https://api.medux.io`

Remove a logo from a video using an optional logo reference and motion mode.

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
| `input_video_file_id` | `string` | Required | `BODY` | Input video file_id. |
| `logo_file_id` | `string` | Optional | `BODY` | Optional logo image file_id used to build the logo mask session. |
| `video_size` | `object` | Optional | `BODY` | Optional original video size hint as [width, height]. |
| `logo_type` | `string` | Optional | `BODY` | Logo motion mode for mask generation. Default: moving. Default: moving.<br>Options: `moving` |
| `model_id` | `string` | Optional | `BODY` | Video logo removal model id. Default: video-logo-removal-default. |
| `title` | `string` | Optional | `BODY` | Optional task title. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `FILE_ID` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/process/video/video_logo_removal \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"input_video_file_id":"FILE_ID","logo_type":"moving","model_id":"video-logo-removal-default"}'
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
- Tool: `medux_video_logo_removal`
- Result type: `—`


## Related APIs

- [Sync Task](../../infra/sync-task/) — Refresh task state from the upstream provider.
- [Get Process Task](../../process/get-process-task/) — Read the current state of a processing task.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/process/video-logo-removal)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
