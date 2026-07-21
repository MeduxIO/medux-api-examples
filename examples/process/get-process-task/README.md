# Get Process Task

Read the current state of a processing task.

## Endpoint

```http
GET /api/app/v1/process/tasks/{task_id}
```

Base URL: `https://api.medux.io`

Return the current state of a media processing task.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Requires a task_id returned by a processing request.
- Use this to poll processing workflows.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `task_id` | `string` | Required | `PATH` | Identifier of the Medux task to retrieve or synchronize. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `TASK_ID` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X GET https://api.medux.io/api/app/v1/process/tasks/TASK_ID \
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
| `code` | `int32` | Optional | `RESPONSE` | Application response code.<br><br>\| Code \| Meaning \|<br>\| ---- \| ------- \|<br>\| `0` \| OK \|<br>\| `1404` \| Provider returned an error \|<br>\| `1405` \| Provider request timed out \|<br>\| `13` \| Authentication is required \|<br>\| `15` \| Resource not found \|<br>\| `99` \| Server error \|<br>Options: `0`, `1404`, `1405`, `13`, `15`, `99` |
| `data.task` | `object` | Optional | `RESPONSE` | Task record created or returned by an asynchronous operation. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `provider error`, `provider timeout`, `unauthenticated`, `not found`, `server error` |

### Response handling

This response can include `data.task`. Persist the returned task ID and use the [relevant task-status endpoint](../../process/get-process-task/) until the task reaches a terminal state. Do not treat HTTP 200 alone as proof that asynchronous media processing has completed.

Application response codes and meanings are reproduced in the response-field table above from the official reference. Handle the documented non-success messages explicitly: `provider error`, `provider timeout`, `unauthenticated`, `not found`, `server error`.

## Official sample

No official media sample is currently documented for this endpoint.

## MCP alternative

This endpoint does not currently document a hosted MCP tool.

## Related APIs

- No related endpoints documented.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/process/get-process-task)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
