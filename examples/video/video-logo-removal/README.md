# Logo Removal

Remove a logo from a video using one or more logo references and motion mode.

## Endpoint

```http
POST /api/app/v1/process/video/video_logo_removal
```

Base URL: `https://api.medux.io`

Remove a logo from a video using one or more logo references and motion mode.

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
| `logo_file_id` | `array<string>` | Optional | `BODY` | One logo image file_id or a list of logo image file_ids used to build the logo mask session. |
| `video_size` | `object` | Optional | `BODY` | Optional original video size hint as [width, height]. |
| `logo_type` | `string` | Optional | `BODY` | Logo motion mode for mask generation. Default: default.<br>Options: `default`, `tiktok`, `heygen`, `veo`, `keling`, `instagram`, `luma`, `pika`, `snapchat`, `pixverse` |
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
  -d '{"input_video_file_id":"FILE_ID","logo_type":"default","model_id":"video-logo-removal-default"}'
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

No official media sample is currently documented for this endpoint.

## MCP alternative

The same capability is optionally available through Medux MCP.

- MCP endpoint: `https://medux.io/mcp`
- Tool: `medux_video_logo_removal`
- Result type: `—`


## Related APIs

- [Sync Task](../../infra/sync-task/) — Refresh task state from the upstream provider.


<!-- medux-pages:start -->
## Try it on medux.io

| Type | Page |
| --- | --- |
| Playground | [medux.io/playground/video/video-logo-removal](https://medux.io/playground/video/video-logo-removal) |
| Workshop | [medux.io/workshop/remove](https://medux.io/workshop/remove) |
| Workshop | [medux.io/workshop/remove/filmora-video-logo-removal](https://medux.io/workshop/remove/filmora-video-logo-removal) |
| Workshop | [medux.io/workshop/remove/heygen-video-logo-removal](https://medux.io/workshop/remove/heygen-video-logo-removal) |
| Workshop | [medux.io/workshop/remove/inshot-video-logo-removal](https://medux.io/workshop/remove/inshot-video-logo-removal) |
| Workshop | [medux.io/workshop/remove/instagram-video-logo-removal](https://medux.io/workshop/remove/instagram-video-logo-removal) |
| Workshop | [medux.io/workshop/remove/kling-video-logo-removal](https://medux.io/workshop/remove/kling-video-logo-removal) |
| Workshop | [medux.io/workshop/remove/luma-video-logo-removal](https://medux.io/workshop/remove/luma-video-logo-removal) |
| Workshop | [medux.io/workshop/remove/pika-video-logo-removal](https://medux.io/workshop/remove/pika-video-logo-removal) |
| Workshop | [medux.io/workshop/remove/pixverse-video-logo-removal](https://medux.io/workshop/remove/pixverse-video-logo-removal) |
| Workshop | [medux.io/workshop/remove/snapchat-video-logo-removal](https://medux.io/workshop/remove/snapchat-video-logo-removal) |
| Workshop | [medux.io/workshop/remove/tiktok-video-logo-removal](https://medux.io/workshop/remove/tiktok-video-logo-removal) |
| Workshop | [medux.io/workshop/remove/veo-video-logo-removal](https://medux.io/workshop/remove/veo-video-logo-removal) |

- MCP tool: `medux_video_logo_removal`
- Claude MCP example: [examples/claude/process/process-video-logo-removal](https://github.com/MeduxIO/medux-mcp-examples/tree/main/examples/claude/process/process-video-logo-removal)
- Codex MCP example: [examples/codex/process/process-video-logo-removal](https://github.com/MeduxIO/medux-mcp-examples/tree/main/examples/codex/process/process-video-logo-removal)
- All pages: [Playground and Workshop pages](https://github.com/MeduxIO/medux-mcp-examples/blob/main/docs/workshop-pages.md)
<!-- medux-pages:end -->

## Source of truth

- [Official API Reference](https://medux.io/api-reference/video/video-logo-removal)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
