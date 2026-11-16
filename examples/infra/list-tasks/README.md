# List Tasks

List account media tasks with optional status and pagination filters. Returns clone, generation, and processing task records for dashboards, history, and workflow monitoring.

## Endpoint

```http
GET /api/app/v1/tasks
```

Base URL: `https://api.medux.io`

List task records for the current user.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Try it returns the current account's task history.
- Use this for history views or background polling dashboards.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `cursor` | `string` | Optional | `QUERY` | Opaque pagination cursor returned by the previous page. |
| `limit` | `int32` | Optional | `QUERY` | Maximum number of records to return in this page. |
| `status` | `string` | Optional | `QUERY` | Filter records by lifecycle status.<br>Options: `TASK_STATUS_UNDEFINED`, `QUEUED`, `PROCESSING`, `SUCCEEDED`, `FAILED`, `EXPIRED` |
| `media_type` | `string` | Optional | `QUERY` | Media-type filter for the returned records. |
| `capability_id` | `string` | Optional | `QUERY` | Filter records by Medux capability identifier. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `CURSOR` — optional query parameter `cursor`.
- `LIMIT` — optional query parameter `limit`.
- `STATUS` — optional query parameter `status`.
- `MEDIA_TYPE` — optional query parameter `media_type`.
- `CAPABILITY_ID` — optional query parameter `capability_id`.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X GET 'https://api.medux.io/api/app/v1/tasks?cursor=CURSOR&limit=LIMIT&status=QUEUED&media_type=MEDIA_TYPE&capability_id=CAPABILITY_ID' \
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

- [Official API Reference](https://medux.io/api-reference/infra/list-tasks)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
