# Create Audio Driven Video

Generate a video from a reusable avatar and source audio asset.

## Endpoint

```http
POST /api/app/v1/generate/video/audio_driven
```

Base URL: `https://api.medux.io`

Generate an avatar video by pairing a reusable avatar with an uploaded audio file.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Prepare avatar and audio assets before calling this endpoint.
- Requires avatar_asset_id from your Media Assets or official public assets, plus audio_file_id.
- Also accepts optional duration_seconds, links, clarity, aspect_ratio, and model.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `aspect_ratio` | `string` | Optional | `BODY` | Requested output aspect ratio, such as 16:9 or 9:16. |
| `audio_file_id` | `string` | Required | `BODY` | Identifier of the uploaded audio file used by this operation. |
| `avatar_asset_id` | `string` | Required | `BODY` | Reusable avatar asset ID owned by the current user or listed as an official public asset. |
| `clarity` | `string` | Optional | `BODY` | Requested output resolution label, such as 1080P or 2K. |
| `duration_seconds` | `int32` | Optional | `BODY` | Requested output duration, in seconds. |
| `links` | `array<string>` | Optional | `BODY` | Optional reference links submitted from the Playground form. |
| `model` | `string` | Optional | `BODY` | Generation model label or version selected in the Playground form. |
| `model_id` | `string` | Optional | `BODY` | Stable public Medux model identifier. |
| `title` | `string` | Optional | `BODY` | Optional user-facing title for the task or generated asset. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `ASPECT_RATIO` — replace the corresponding placeholder in the official example.
- `AUDIO_FILE_ID` — replace the corresponding placeholder in the official example.
- `AVATAR_ASSET_ID` — replace the corresponding placeholder in the official example.
- `CLARITY` — replace the corresponding placeholder in the official example.
- `MODEL` — replace the corresponding placeholder in the official example.
- `MODEL_ID` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/generate/video/audio_driven \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"aspect_ratio":"ASPECT_RATIO","audio_file_id":"AUDIO_FILE_ID","avatar_asset_id":"AVATAR_ASSET_ID","clarity":"CLARITY","duration_seconds":1,"links":["https://example.com/reference"],"model":"MODEL","model_id":"MODEL_ID","title":"Demo title"}'
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
| `code` | `int32` | Optional | `RESPONSE` | Application response code. Full catalog: [error-codes.md](../../../docs/error-codes.md).<br>- `0` — OK<br>- `12` — Invalid input<br>- `1410` — Invalid model<br>- `1409` — Paid plan required<br>- `1401` — Insufficient credits<br>- `1402` — Asset category does not match this operation<br>- `1407` — Reserved media-domain error; meaning not published in the reference.<br>- `1408` — Reserved media-domain error; meaning not published in the reference.<br>- `1404` — Provider returned an error<br>- `1405` — Provider request timed out<br>- `13` — Authentication is required<br>- `16` — Rate limit exceeded<br>- `99` — Server error |
| `data.asset` | `object` | Optional | `RESPONSE` | Asset created or returned by the operation when available. |
| `data.paid_plan_required` | `object` | Optional | `RESPONSE` | Paid-plan requirement details when the selected capability is unavailable on the current plan. |
| `data.task` | `object` | Optional | `RESPONSE` | Task record created or returned by an asynchronous operation. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `asset category mismatch`, `asset locked`, `asset expired`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error` |

### Response handling

This response can include `data.task`. Persist the returned task ID and use the [relevant task-status endpoint](../../generate/get-creation-task/) until the task reaches a terminal state. Do not treat HTTP 200 alone as proof that asynchronous media processing has completed.

The response-field table above lists the `code` values this endpoint can return, each with its meaning. Handle the documented non-success messages explicitly: `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `asset category mismatch`, `asset locked`, `asset expired`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error`. See [error-codes.md](../../../docs/error-codes.md) for the full catalog and retry guidance.

## Official sample

### Official audio-driven talking video

- Sample ID: `sample_generate_video_audio_driven_001`
- Input: `avatar_asset_id=official_avatar_demo_001`, `audio_file_id={audio_file_id}`
- Output: `output_url=Official example video output`
- Model: `talking-video-audio-standard`
- Minimum plan: `free`
- Preview: [Open documented sample](https://medux-cdn-dev.hifly.cc/demo/G7qPpzNfYQ.mp4)

## MCP alternative

The same capability is optionally available through Medux MCP.

- MCP endpoint: `https://mcp.medux.io/api/mcp/v1`
- Tool: `medux_video_create_audio_driven`
- Result type: `VIDEO`

Example prompt:

```text
Create a 7 second 1080P 16:9 talking video using avatar_asset_id {avatar_asset_id} and audio_file_id {audio_file_id}. Use model_id talking-video-audio-standard.
```


## Related APIs

- No related endpoints documented.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/generate/create-audio-driven-video)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
