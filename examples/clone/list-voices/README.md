# List Voices

List reusable AI voice assets with optional filters. Returns voice IDs and lifecycle states for text-to-speech, narration, and talking-avatar voice selection.

## Endpoint

```http
GET /api/app/v1/clone/voices
```

Base URL: `https://api.medux.io`

List current user's reusable voice assets.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Try it lists the current user's voice assets.
- Only voice assets are returned.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `cursor` | `string` | Optional | `QUERY` | Opaque pagination cursor returned by the previous page. |
| `limit` | `int32` | Optional | `QUERY` | Maximum number of records to return in this page. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `CURSOR` — optional query parameter `cursor`.
- `LIMIT` — optional query parameter `limit`.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X GET 'https://api.medux.io/api/app/v1/clone/voices?cursor=CURSOR&limit=LIMIT' \
  -H "Authorization: Bearer $MEDUX_API_KEY"
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
| `code` | `int32` | Optional | `RESPONSE` | Application response code. Full catalog: [error-codes.md](../../../docs/error-codes.md).<br>- `0` — OK<br>- `12` — Invalid input<br>- `13` — Authentication is required<br>- `99` — Server error |
| `data.items` | `array<object>` | Optional | `RESPONSE` | Collection of records returned by a list operation. |
| `data.next_cursor` | `string` | Optional | `RESPONSE` | Opaque cursor to request the next page; absent or empty when no next page is available. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `invalid input`, `unauthenticated`, `server error` |

### Response handling

Check both the HTTP status and the application-level `code` and `message` fields before consuming `data`.

The response-field table above lists the `code` values this endpoint can return, each with its meaning. Handle the documented non-success messages explicitly: `invalid input`, `unauthenticated`, `server error`. See [error-codes.md](../../../docs/error-codes.md) for the full catalog and retry guidance.

## Official sample

No official media sample is currently documented for this endpoint.

## MCP alternative

This endpoint does not currently document a hosted MCP tool.

## Related APIs

- No related endpoints documented.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/clone/list-voices)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
