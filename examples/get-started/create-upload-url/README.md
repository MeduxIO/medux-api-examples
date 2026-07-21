# Create Upload URL

Create a direct upload URL before recording the uploaded file as an asset.

## Endpoint

```http
POST /api/app/v1/upload_urls
```

Base URL: `https://api.medux.io`

Create a pre-signed upload URL and file reference for a direct client upload.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Try it is available after login because the returned upload target is account-scoped.
- Use this as the first step in most Playground and agent flows.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `extension` | `string` | Optional | `BODY` | File extension without a leading dot, such as mp4. |
| `media_type` | `string` | Optional | `BODY` | Media type used to validate extension and build the object path.<br><br>Allowed values:<br>- `MEDIA_TYPE_UNDEFINED` - Not specified.<br>- `VIDEO` - Video file, such as mp4.<br>- `AUDIO` - Audio file, such as mp3.<br>- `IMAGE` - Image file, such as png.<br>- `DOCUMENT` - Document file, such as md or docx.<br>Options: `MEDIA_TYPE_UNDEFINED`, `VIDEO`, `AUDIO`, `IMAGE`, `DOCUMENT` |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/upload_urls \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"extension":"png","media_type":"VIDEO"}'
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
| `code` | `int32` | Optional | `RESPONSE` | Application response code.<br><br>\| Code \| Meaning \|<br>\| ---- \| ------- \|<br>\| `0` \| OK \|<br>\| `12` \| Invalid input \|<br>\| `13` \| Authentication is required \|<br>\| `16` \| Rate limit exceeded \|<br>\| `99` \| Server error \|<br>Options: `0`, `12`, `13`, `16`, `99` |
| `data.content_type` | `string` | Optional | `RESPONSE` | Content-Type expected by the direct upload request. |
| `data.file` | `object` | Optional | `RESPONSE` | File reference to pass into later media APIs. |
| `data.upload_url` | `string` | Optional | `RESPONSE` | Pre-signed URL the client should upload the file to. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `invalid input`, `unauthenticated`, `rate limit`, `server error` |

### Response handling

Check both the HTTP status and the application-level `code` and `message` fields before consuming `data`.

Application response codes and meanings are reproduced in the response-field table above from the official reference. Handle the documented non-success messages explicitly: `invalid input`, `unauthenticated`, `rate limit`, `server error`.

## Official sample

No official media sample is currently documented for this endpoint.

## MCP alternative

This endpoint does not currently document a hosted MCP tool.

## Related APIs

- [File reference](../../infra/create-asset/) — Persist the uploaded file as a file reference.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/get-started/create-upload-url)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
