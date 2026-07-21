# Create Asset

Persist a reusable avatar or voice asset record.

## Endpoint

```http
POST /api/app/v1/assets
```

Base URL: `https://api.medux.io`

Create an asset record from a file that was uploaded through a direct upload URL.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Requires reusable asset metadata.
- Uploaded MEDIA files use file_id directly and do not need this endpoint.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `category` | `string` | Optional | `BODY` | Asset category, used for validation and later rendering.<br><br>Allowed values:<br>- `CATEGORY_UNDEFINED` - Not specified.<br>- `MEDIA` - Uploaded source media.<br>- `AVATAR` - Reusable avatar asset.<br>- `VOICE` - Reusable voice asset.<br>Options: `CATEGORY_UNDEFINED`, `MEDIA`, `AVATAR`, `VOICE` |
| `file_size_bytes` | `int64` | Optional | `BODY` | Original file size, in bytes. |
| `name` | `string` | Optional | `BODY` | Display name provided by the user. This value may be empty. |
| `storage_object.key` | `string` | Optional | `BODY` | Storage object key returned by the upload flow. |
| `storage_object.url` | `string` | Optional | `BODY` | Storage object URL associated with the uploaded file. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `NAME` — replace the corresponding placeholder in the official example.
- `STORAGE_OBJECT_KEY` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/assets \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"category":"MEDIA","file_size_bytes":1,"name":"NAME","storage_object":{"key":"STORAGE_OBJECT_KEY","url":"https://example.com/callback"}}'
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
| `code` | `int32` | Optional | `RESPONSE` | Application response code.<br><br>\| Code \| Meaning \|<br>\| ---- \| ------- \|<br>\| `0` \| OK \|<br>\| `12` \| Invalid input \|<br>\| `16` \| Rate limit exceeded \|<br>\| `99` \| Server error \|<br>Options: `0`, `12`, `1406`, `13`, `16`, `99` |
| `data.asset` | `object` | Optional | `RESPONSE` | Asset created or returned by the operation when available. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `invalid input`, `asset limit reached`, `unauthenticated`, `rate limit`, `server error` |

### Response handling

Check both the HTTP status and the application-level `code` and `message` fields before consuming `data`.

Application response codes and meanings are reproduced in the response-field table above from the official reference. Handle the documented non-success messages explicitly: `invalid input`, `asset limit reached`, `unauthenticated`, `rate limit`, `server error`.

## Official sample

No official media sample is currently documented for this endpoint.

## MCP alternative

This endpoint does not currently document a hosted MCP tool.

## Related APIs

- No related endpoints documented.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/infra/create-asset)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
