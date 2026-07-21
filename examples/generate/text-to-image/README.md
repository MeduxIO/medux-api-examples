# Create Text to Image

Generate an image from a text prompt.

## Endpoint

```http
POST /api/app/v1/generate/image/text_to_image
```

Base URL: `https://api.medux.io`

Generate an image from a text prompt.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Requires a valid Authorization header and the configured request body.
- Successful requests return a Medux task record immediately. Use the task query or sync endpoints to track completion.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `prompt` | `string` | Required | `BODY` | Prompt text used to generate the image. |
| `negative_prompt` | `string` | Optional | `BODY` | Optional negative prompt. |
| `height` | `integer` | Optional | `BODY` | Output image height. Default: 1024. |
| `width` | `integer` | Optional | `BODY` | Output image width. Default: 1024. |
| `seed` | `integer` | Optional | `BODY` | Random seed. Use -1 to auto-generate. Default: -1. |
| `num_inference_steps` | `integer` | Optional | `BODY` | Number of inference steps. Default: 9. |
| `guidance_scale` | `number` | Optional | `BODY` | Guidance scale. Default: 0.0. |
| `cfg_normalization` | `boolean` | Optional | `BODY` | Whether to enable CFG normalization. Default: false. |
| `cfg_truncation` | `number` | Optional | `BODY` | CFG truncation value. Default: 1.0. |
| `max_sequence_length` | `integer` | Optional | `BODY` | Maximum text sequence length. Default: 512. |
| `model_id` | `string` | Optional | `BODY` | Text-to-image model id. Default: text-to-image-default. |
| `title` | `string` | Optional | `BODY` | Optional task title. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `PROMPT` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/generate/image/text_to_image \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"cfg_normalization":false,"cfg_truncation":1,"guidance_scale":0,"height":1024,"max_sequence_length":512,"model_id":"text-to-image-default","num_inference_steps":9,"prompt":"PROMPT","seed":-1,"width":1024}'
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

This response can include `data.task`. Persist the returned task ID and use the [relevant task-status endpoint](../../generate/get-creation-task/) until the task reaches a terminal state. Do not treat HTTP 200 alone as proof that asynchronous media processing has completed.

The response-field table above lists the `code` values this endpoint can return, each with its meaning. Handle the documented non-success messages explicitly: `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error`. See [error-codes.md](../../../docs/error-codes.md) for the full catalog and retry guidance.

## Official sample

No official media sample is currently documented for this endpoint.

## MCP alternative

The same capability is optionally available through Medux MCP.

- MCP endpoint: `https://mcp.medux.io/api/mcp/v1`
- Tool: `medux_text_to_image`
- Result type: `—`


## Related APIs

- [Sync Task](../../infra/sync-task/) — Refresh task state from the upstream provider.
- [Get Creation Task](../../generate/get-creation-task/) — Read the current state of a generation task.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/generate/text-to-image)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
