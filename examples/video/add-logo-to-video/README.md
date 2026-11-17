# Add Logo to Video

Overlay a logo image onto a video.

## Endpoint

```http
POST /api/app/v1/process/video/add_logo_to_video
```

Base URL: `https://api.medux.io`

Overlay a logo image onto a video.

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
| `video_file_id` | `string` | Required | `BODY` | Input video file_id. |
| `logo_file_id` | `string` | Required | `BODY` | Logo image file_id. |
| `x` | `integer` | Optional | `BODY` | Logo X position, default 10. Default: 10. |
| `y` | `integer` | Optional | `BODY` | Logo Y position, default 10. Default: 10. |
| `logo_width` | `integer` | Optional | `BODY` | Logo width in pixels. If set, logo_height must also be set. |
| `logo_height` | `integer` | Optional | `BODY` | Logo height in pixels. |
| `model_id` | `string` | Optional | `BODY` | Model Default: add-logo-to-video-default. |
| `title` | `string` | Optional | `BODY` | Optional task title. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `FILE_ID` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/process/video/add_logo_to_video \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"logo_file_id":"FILE_ID","model_id":"add-logo-to-video-default","video_file_id":"FILE_ID","x":10,"y":10}'
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
| `code` | `int32` | Optional | `RESPONSE` | Application response code. Full catalog: [error-codes.md](../../../docs/error-codes.md).<br>- `0` — OK<br>- `12` — Invalid input<br>- `1410` — Invalid model<br>- `1409` — Paid plan required<br>- `1401` — Insufficient credits<br>- `1404` — Provider returned an error<br>- `1405` — Provider request timed out<br>- `13` — Authentication is required<br>- `16` — Rate limit exceeded<br>- `99` — Server error |
| `data.asset` | `object` | Optional | `RESPONSE` | Asset created or returned by the operation when available. |
| `data.paid_plan_required` | `object` | Optional | `RESPONSE` | Paid-plan requirement details when the selected capability is unavailable on the current plan. |
| `data.task` | `object` | Optional | `RESPONSE` | Task record created or returned by an asynchronous operation. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error` |

### Response handling

This response can include `data.task`. Persist the returned task ID and use the [relevant task-status endpoint](../../infra/get-task/) until the task reaches a terminal state. Do not treat HTTP 200 alone as proof that asynchronous media processing has completed.

The response-field table above lists the `code` values this endpoint can return, each with its meaning. Handle the documented non-success messages explicitly: `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error`. See [error-codes.md](../../../docs/error-codes.md) for the full catalog and retry guidance.

## Official sample

### Official add logo to video sample

- Sample ID: `sample_add_logo_to_video_001`
- Input: `video_file_id={file_id}`, `logo_file_id={file_id}`, `x=10`, `y=10`
- Output: —
- Model: `add-logo-to-video-default`
- Minimum plan: `free`
- Preview: currently unavailable; the URL published by the official reference returned HTTP 404 during validation. The original URL remains in `reference.json`.

## MCP alternative

The same capability is optionally available through Medux MCP.

- MCP endpoint: `https://medux.io/mcp`
- Tool: `medux_add_logo_to_video`
- Result type: `—`


## Related APIs

- [Sync Task](../../infra/sync-task/) — Refresh task state from the upstream provider.


<!-- medux-pages:start -->
## Try it on medux.io

| Type | Page |
| --- | --- |
| Playground | [medux.io/playground/video/add-logo-to-video](https://medux.io/playground/video/add-logo-to-video) |

- MCP tool: `medux_add_logo_to_video`
- Claude MCP example: [examples/claude/media/add-logo-to-video](https://github.com/MeduxIO/medux-mcp-examples/tree/main/examples/claude/media/add-logo-to-video)
- Codex MCP example: [examples/codex/process/add-logo-to-video](https://github.com/MeduxIO/medux-mcp-examples/tree/main/examples/codex/process/add-logo-to-video)
- All pages: [Playground and Workshop pages](https://github.com/MeduxIO/medux-mcp-examples/blob/main/docs/workshop-pages.md)
<!-- medux-pages:end -->

## Source of truth

- [Official API Reference](https://medux.io/api-reference/video/add-logo-to-video)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
