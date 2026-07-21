# Edit Voice Parameters

Adjust voice parameters for an existing reusable voice asset.

## Endpoint

```http
POST /api/app/v1/clone/voice/{voice_asset_id}/parameters
```

Base URL: `https://api.medux.io`

Update tuning parameters for an existing reusable voice asset.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Requires an existing voice_asset_id.
- Provide at least one change such as speed, tone, emotion, or title.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `voice_asset_id` | `string` | Required | `PATH` | Identifier of the reusable Medux voice asset. |
| `emotion` | `int32` | Optional | `BODY` | Voice emotion adjustment value. |
| `speed` | `int32` | Optional | `BODY` | Voice or media speed adjustment value. |
| `title` | `string` | Optional | `BODY` | Optional user-facing title for the task or generated asset. |
| `tone` | `int32` | Optional | `BODY` | Voice tone adjustment value. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `VOICE_ASSET_ID` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/clone/voice/VOICE_ASSET_ID/parameters \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"emotion":1,"speed":1,"title":"Demo title","tone":1}'
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
| `code` | `int32` | Optional | `RESPONSE` | Application response code.<br><br>\| Code \| Meaning \|<br>\| ---- \| ------- \|<br>\| `0` \| OK \|<br>\| `12` \| Invalid input \|<br>\| `1401` \| Insufficient credits \|<br>\| `1404` \| Provider returned an error \|<br>\| `1405` \| Provider request timed out \|<br>\| `13` \| Authentication is required \|<br>\| `16` \| Rate limit exceeded \|<br>\| `99` \| Server error \|<br>Options: `0`, `12`, `1410`, `1409`, `1401`, `1407`, `1408`, `1404`, `1405`, `13`, `16`, `99` |
| `data.asset` | `object` | Optional | `RESPONSE` | Asset created or returned by the operation when available. |
| `data.paid_plan_required` | `object` | Optional | `RESPONSE` | Paid-plan requirement details when the selected capability is unavailable on the current plan. |
| `data.task` | `object` | Optional | `RESPONSE` | Task record created or returned by an asynchronous operation. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `asset locked`, `asset expired`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error` |

### Response handling

This response can include `data.task`. Persist the returned task ID and use the [relevant task-status endpoint](../../clone/get-voice-task/) until the task reaches a terminal state. Do not treat HTTP 200 alone as proof that asynchronous media processing has completed.

Application response codes and meanings are reproduced in the response-field table above from the official reference. Handle the documented non-success messages explicitly: `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `asset locked`, `asset expired`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error`.

## Official sample

No official media sample is currently documented for this endpoint.

## MCP alternative

This endpoint does not currently document a hosted MCP tool.

## Related APIs

- No related endpoints documented.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/clone/edit-voice-parameters)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
