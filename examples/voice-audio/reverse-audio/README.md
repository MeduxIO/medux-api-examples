# Reverse Audio

Reverse an audio file.

## Endpoint

```http
POST /api/app/v1/process/audio/reverse_audio
```

Base URL: `https://api.medux.io`

Reverse an audio file.

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
| `input_file_id` | `string` | Required | `BODY` | Input audio file_id. |
| `model_id` | `string` | Optional | `BODY` | Model Default: reverse-audio-default. |
| `title` | `string` | Optional | `BODY` | Optional task title. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `FILE_ID` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/process/audio/reverse_audio \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"input_file_id":"FILE_ID","model_id":"reverse-audio-default"}'
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

### Official reverse audio sample

- Sample ID: `sample_reverse_audio_001`
- Input: `input_file_id={file_id}`
- Output: —
- Model: `reverse-audio-default`
- Minimum plan: `free`
- Preview: currently unavailable; the URL published by the official reference returned HTTP 404 during validation. The original URL remains in `reference.json`.

## MCP alternative

The same capability is optionally available through Medux MCP.

- MCP endpoint: `https://medux.io/mcp`
- Tool: `medux_reverse_audio`
- Result type: `—`


## Related APIs

- [Sync Task](../../infra/sync-task/) — Refresh task state from the upstream provider.


<!-- medux-pages:start -->
## Try it on medux.io

| Type | Page |
| --- | --- |
| Playground | [medux.io/playground/audio/reverse-audio](https://medux.io/playground/audio/reverse-audio) |

- MCP tool: `medux_reverse_audio`
- Claude MCP example: [examples/claude/media/media-reverse-audio](https://github.com/MeduxIO/medux-mcp-examples/tree/main/examples/claude/media/media-reverse-audio)
- Codex MCP example: [examples/codex/media/media-reverse-audio](https://github.com/MeduxIO/medux-mcp-examples/tree/main/examples/codex/media/media-reverse-audio)
- All pages: [Playground and Workshop pages](https://github.com/MeduxIO/medux-mcp-examples/blob/main/docs/workshop-pages.md)
<!-- medux-pages:end -->

## Source of truth

- [Official API Reference](https://medux.io/api-reference/voice-audio/reverse-audio)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
