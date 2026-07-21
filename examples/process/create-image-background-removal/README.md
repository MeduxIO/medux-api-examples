# Create Image Background Removal

Submit an image background removal processing task.

## Endpoint

```http
POST /api/app/v1/process/image/background_removal
```

Base URL: `https://api.medux.io`

Create an image processing task that removes the background from an uploaded image.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Upload the source image and create an asset before calling this endpoint.
- Requires an existing image file_id.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `file_id` | `string` | Required | `BODY` | Identifier of a file created through the Medux upload flow. |
| `region.height` | `int32` | Optional | `BODY` | Height of the target processing region. |
| `region.width` | `int32` | Optional | `BODY` | Width of the target processing region. |
| `region.x` | `int32` | Optional | `BODY` | X coordinate of the region's top-left corner in pixels. |
| `region.y` | `int32` | Optional | `BODY` | Y coordinate of the region's top-left corner in pixels. |
| `title` | `string` | Optional | `BODY` | Optional user-facing title for the task or generated asset. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `FILE_ID` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/process/image/background_removal \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"file_id":"FILE_ID","region":{"height":1,"width":1,"x":1,"y":1},"title":"Demo title"}'
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
| `code` | `int32` | Optional | `RESPONSE` | Application response code.<br><br>\| Code \| Meaning \|<br>\| ---- \| ------- \|<br>\| `0` \| OK \|<br>\| `12` \| Invalid input \|<br>\| `1401` \| Insufficient credits \|<br>\| `1404` \| Provider returned an error \|<br>\| `1405` \| Provider request timed out \|<br>\| `13` \| Authentication is required \|<br>\| `16` \| Rate limit exceeded \|<br>\| `99` \| Server error \|<br>Options: `0`, `12`, `1410`, `1409`, `1401`, `1404`, `1405`, `13`, `16`, `99` |
| `data.asset` | `object` | Optional | `RESPONSE` | Asset created or returned by the operation when available. |
| `data.paid_plan_required` | `object` | Optional | `RESPONSE` | Paid-plan requirement details when the selected capability is unavailable on the current plan. |
| `data.task` | `object` | Optional | `RESPONSE` | Task record created or returned by an asynchronous operation. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error` |

### Response handling

This response can include `data.task`. Persist the returned task ID and use the [relevant task-status endpoint](../../process/get-process-task/) until the task reaches a terminal state. Do not treat HTTP 200 alone as proof that asynchronous media processing has completed.

Application response codes and meanings are reproduced in the response-field table above from the official reference. Handle the documented non-success messages explicitly: `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error`.

## Official sample

### Official image background removal

- Sample ID: `sample_process_image_background_removal_001`
- Input: `file_id={file_id}`, `source=Official sample image for testing`
- Output: `output_url=Official example image output`
- Model: `image-background-removal-standard`
- Minimum plan: `free`
- Preview: [Open documented sample](https://medux-cdn-dev.hifly.cc/demo/3460404a-0df9-4ca0-bb50-4f1e3fa167cd.png)

## MCP alternative

The same capability is optionally available through Medux MCP.

- MCP endpoint: `https://mcp.medux.io/api/mcp/v1`
- Tool: `medux_image_remove_background`
- Result type: `IMAGE`

Example prompt:

```text
Remove the background from the uploaded image {file_id}.
```


## Related APIs

- No related endpoints documented.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/process/create-image-background-removal)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
