# Create Avatar by Image

Start an avatar clone task from a source image asset.

## Endpoint

```http
POST /api/app/v1/clone/avatar/by_image
```

Base URL: `https://api.medux.io`

Create a reusable avatar asset from an uploaded image file.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Requires a valid image file_id.
- Use a clear portrait-style image for best results.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `file_id` | `string` | Required | `BODY` | Identifier of a file created through the Medux upload flow. |
| `title` | `string` | Optional | `BODY` | Optional user-facing title for the task or generated asset. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `FILE_ID` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/clone/avatar/by_image \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"file_id":"FILE_ID","title":"Demo title"}'
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
| `code` | `int32` | Optional | `RESPONSE` | Application response code. Full catalog: [error-codes.md](../../../docs/error-codes.md).<br>- `0` — OK<br>- `12` — Invalid input<br>- `1410` — Invalid model<br>- `1409` — Paid plan required<br>- `1401` — Insufficient credits<br>- `1406` — Reserved media-domain error; meaning not published in the reference.<br>- `1402` — Asset category does not match this operation<br>- `1404` — Provider returned an error<br>- `1405` — Provider request timed out<br>- `13` — Authentication is required<br>- `16` — Rate limit exceeded<br>- `99` — Server error |
| `data.asset` | `object` | Optional | `RESPONSE` | Asset created or returned by the operation when available. |
| `data.paid_plan_required` | `object` | Optional | `RESPONSE` | Paid-plan requirement details when the selected capability is unavailable on the current plan. |
| `data.task` | `object` | Optional | `RESPONSE` | Task record created or returned by an asynchronous operation. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `asset limit reached`, `asset category mismatch`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error` |

### Response handling

This response can include `data.task`. Persist the returned task ID and use the [relevant task-status endpoint](../../clone/get-avatar-task/) until the task reaches a terminal state. Do not treat HTTP 200 alone as proof that asynchronous media processing has completed.

The response-field table above lists the `code` values this endpoint can return, each with its meaning. Handle the documented non-success messages explicitly: `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `asset limit reached`, `asset category mismatch`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error`. See [error-codes.md](../../../docs/error-codes.md) for the full catalog and retry guidance.

## Official sample

### Official avatar clone from image

- Sample ID: `sample_clone_avatar_by_image_001`
- Input: `file_id={file_id}`, `source=Official sample portrait image for testing`
- Output: `avatar_asset_id=official_avatar_demo_image_001`
- Model: `avatar-image-clone-standard`
- Minimum plan: `free`
- Preview: [Open documented sample](https://medux-cdn-dev.hifly.cc/demo/3460404a-0df9-4ca0-bb50-4f1e3fa167cd.png)

## MCP alternative

The same capability is optionally available through Medux MCP.

- MCP endpoint: `https://mcp.medux.io/api/mcp/v1`
- Tool: `medux_avatar_clone_by_image`
- Result type: `AVATAR_ASSET`

Example prompt:

```text
Clone a reusable avatar from the uploaded portrait image {file_id}. Title it Official avatar image clone sample.
```


## Related APIs

- [List Avatars](../../clone/list-avatars/) — Review reusable avatar assets.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/clone/create-avatar-by-image)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
