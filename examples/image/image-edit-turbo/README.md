# Image Edit Turbo

Edit one or more images from a text prompt.

## Endpoint

```http
POST /api/app/v1/generate/image/image_edit_turbo
```

Base URL: `https://api.medux.io`

Edit one or more images from a text prompt.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Upload each source file and create file references before calling this endpoint.
- Successful requests return a Medux task record immediately. Use the task query or sync endpoints to track completion.
- All file inputs must be uploaded and persisted as file references before submission.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `image_file_ids` | `array<string>` | Required | `BODY` | Input image file_id list. |
| `prompt` | `string` | Required | `BODY` | Prompt text describing the requested image edit. |
| `negative_prompt` | `string` | Optional | `BODY` | Optional negative prompt. |
| `height` | `integer` | Optional | `BODY` | Output image height. Default: 1024. |
| `width` | `integer` | Optional | `BODY` | Output image width. Default: 1024. |
| `model_id` | `string` | Optional | `BODY` | Image editing model id. Default: qwen-image-edit.<br>Options: `qwen-image-edit`, `qwen-image-21`, `minimax-h3-image` |
| `title` | `string` | Optional | `BODY` | Optional task title. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `FILE_ID` — replace the corresponding placeholder in the official example.
- `PROMPT` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/generate/image/image_edit_turbo \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"height":1024,"image_file_ids":["FILE_ID"],"model_id":"qwen-image-edit","prompt":"PROMPT","width":1024}'
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
- Tool: `medux_image_edit`
- Result type: `—`


## Related APIs

- [Sync Task](../../infra/sync-task/) — Refresh task state from the upstream provider.


<!-- medux-pages:start -->
## Try it on medux.io

| Type | Page |
| --- | --- |
| Playground | [medux.io/playground/image/image-edit-turbo](https://medux.io/playground/image/image-edit-turbo) |
| Workshop | [medux.io/workshop/image-edit](https://medux.io/workshop/image-edit) |
| Workshop | [medux.io/workshop/qwen-image-edit](https://medux.io/workshop/qwen-image-edit) |

- MCP tool: `medux_image_edit`
- Claude MCP example: [examples/claude/workshop/image-edit-turbo](https://github.com/MeduxIO/medux-mcp-examples/tree/main/examples/claude/workshop/image-edit-turbo)
- Codex MCP example: [examples/codex/workshop/image-edit-turbo](https://github.com/MeduxIO/medux-mcp-examples/tree/main/examples/codex/workshop/image-edit-turbo)
- All pages: [Playground and Workshop pages](https://github.com/MeduxIO/medux-mcp-examples/blob/main/docs/workshop-pages.md)
<!-- medux-pages:end -->

## Source of truth

- [Official API Reference](https://medux.io/api-reference/image/image-edit-turbo)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
