# Omni Reference to Video

Guide video generation with the reference types supported by your selected model.

## Endpoint

```http
POST /api/app/v1/generate/video/omni_reference_to_video
```

Base URL: `https://api.medux.io`

Generate media with the capability-specific input contract.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Choose an available model and enter a prompt.
- Provide a non-empty prompt and supported image_file_ids, video_file_ids, or audio_file_ids. MiniMax H3 accepts only images; Wan 3.0 limits combined reference video and audio duration to 15 seconds.
- Read generation_options from the model catalog; only listed parameter values are accepted.
- Use clarity for output resolution. Estimate credits with the same parameters before submission.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `aspect_ratio` | `string` | Optional | `BODY` | No additional description is documented. |
| `audio_file_ids` | `array<string>` | Optional | `BODY` | No additional description is documented. |
| `clarity` | `string` | Optional | `BODY` | No additional description is documented. |
| `duration_seconds` | `int32` | Optional | `BODY` | No additional description is documented. |
| `image_file_ids` | `array<string>` | Optional | `BODY` | No additional description is documented. |
| `model_id` | `string` | Optional | `BODY` | No additional description is documented. |
| `prompt` | `string` | Required | `BODY` | Natural-language instruction describing the requested output. |
| `title` | `string` | Optional | `BODY` | Optional user-facing title for the task or generated asset. |
| `video_file_ids` | `array<string>` | Optional | `BODY` | No additional description is documented. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `ASPECT_RATIO` — replace the corresponding placeholder in the official example.
- `AUDIO_FILE_ID` — replace the corresponding placeholder in the official example.
- `CLARITY` — replace the corresponding placeholder in the official example.
- `FILE_ID` — replace the corresponding placeholder in the official example.
- `MODEL_ID` — replace the corresponding placeholder in the official example.
- `PROMPT` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/generate/video/omni_reference_to_video \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"aspect_ratio":"ASPECT_RATIO","audio_file_ids":["AUDIO_FILE_ID"],"clarity":"CLARITY","duration_seconds":1,"image_file_ids":["FILE_ID"],"model_id":"MODEL_ID","prompt":"PROMPT","title":"Demo title","video_file_ids":["FILE_ID"]}'
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
| `code` | `int32` | Optional | `RESPONSE` | Application response code. Full catalog: [error-codes.md](../../../docs/error-codes.md).<br>- `0` — OK<br>- `12` — Invalid input<br>- `1410` — Invalid model<br>- `1409` — Paid plan required<br>- `1401` — Insufficient credits<br>- `13` — Authentication is required<br>- `1404` — Provider returned an error<br>- `99` — Server error |
| `data.asset` | `object` | Optional | `RESPONSE` | Asset created or returned by the operation when available. |
| `data.paid_plan_required` | `object` | Optional | `RESPONSE` | Paid-plan requirement details when the selected capability is unavailable on the current plan. |
| `data.task` | `object` | Optional | `RESPONSE` | Task record created or returned by an asynchronous operation. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `unauthenticated`, `provider error`, `server error` |

### Response handling

This response can include `data.task`. Persist the returned task ID and use the [relevant task-status endpoint](../../infra/get-task/) until the task reaches a terminal state. Do not treat HTTP 200 alone as proof that asynchronous media processing has completed.

The response-field table above lists the `code` values this endpoint can return, each with its meaning. Handle the documented non-success messages explicitly: `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `unauthenticated`, `provider error`, `server error`. See [error-codes.md](../../../docs/error-codes.md) for the full catalog and retry guidance.

## Official sample

No official media sample is currently documented for this endpoint.

## MCP alternative

The same capability is optionally available through Medux MCP.

- MCP endpoint: `https://medux.io/mcp`
- Tool: `medux_video_generate_omni_reference_to_video`
- Result type: `VIDEO`

Example prompt:

```text
Create a video guided by my reference image using Seedance 2.0 Mini.
```


## Related APIs

- No related endpoints documented.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/generate/create-omni-reference-to-video)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
