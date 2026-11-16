# Text to Speech

Convert text with a reusable voice into AI speech audio. Returns an asynchronous text-to-speech task and audio URL for voiceovers, narration, accessibility, and talking-avatar workflows.

## Endpoint

```http
POST /api/app/v1/generate/audio
```

Base URL: `https://api.medux.io`

Create speech audio from text and a reusable voice asset.

## Authentication

- Authentication is required via Authorization header.

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

- Requires a voice_asset_id.
- Requires voice_asset_id from your Media Assets or official public assets, plus non-empty text.
- Also accepts optional links and model.

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
| `Authorization` | `string` | Required | `HEADER` | Bearer token or API key. |
| `links` | `array<string>` | Optional | `BODY` | Optional reference links collected from the Playground form. |
| `model` | `string` | Optional | `BODY` | Selected generation model label or version from the Playground form. |
| `model_id` | `string` | Optional | `BODY` | Stable public Medux model identifier. |
| `text` | `string` | Optional | `BODY` | Text content used to generate speech or media. |
| `title` | `string` | Optional | `BODY` | Optional user-facing title for the task or generated asset. |
| `voice_asset_id` | `string` | Required | `BODY` | Reusable voice asset ID owned by the current user or listed as an official public asset. |

## Environment variables used by the Python and JavaScript examples

- `MEDUX_API_KEY` — required for every request.
- `MODEL` — replace the corresponding placeholder in the official example.
- `MODEL_ID` — replace the corresponding placeholder in the official example.
- `VOICE_ASSET_ID` — replace the corresponding placeholder in the official example.

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
curl -X POST https://api.medux.io/api/app/v1/generate/audio \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"links":["https://example.com/reference"],"model":"MODEL","model_id":"MODEL_ID","text":"Hello from Medux","title":"Demo title","voice_asset_id":"VOICE_ASSET_ID"}'
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
| `code` | `int32` | Optional | `RESPONSE` | Application response code. Full catalog: [error-codes.md](../../../docs/error-codes.md).<br>- `0` — OK<br>- `12` — Invalid input<br>- `1410` — Invalid model<br>- `1409` — Paid plan required<br>- `1401` — Insufficient credits<br>- `1402` — Asset category does not match this operation<br>- `1403` — Voice asset is required<br>- `1407` — Reserved media-domain error; meaning not published in the reference.<br>- `1408` — Reserved media-domain error; meaning not published in the reference.<br>- `1404` — Provider returned an error<br>- `1405` — Provider request timed out<br>- `13` — Authentication is required<br>- `16` — Rate limit exceeded<br>- `99` — Server error |
| `data.asset` | `object` | Optional | `RESPONSE` | Asset created or returned by the operation when available. |
| `data.paid_plan_required` | `object` | Optional | `RESPONSE` | Paid-plan requirement details when the selected capability is unavailable on the current plan. |
| `data.task` | `object` | Optional | `RESPONSE` | Task record created or returned by an asynchronous operation. |
| `message` | `string` | Optional | `RESPONSE` | Human-readable application status or error message.<br>Options: `ok`, `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `asset category mismatch`, `voice asset required`, `asset locked`, `asset expired`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error` |

### Response handling

This response can include `data.task`. Persist the returned task ID and use the [relevant task-status endpoint](../../infra/get-task/) until the task reaches a terminal state. Do not treat HTTP 200 alone as proof that asynchronous media processing has completed.

The response-field table above lists the `code` values this endpoint can return, each with its meaning. Handle the documented non-success messages explicitly: `invalid input`, `invalid model`, `paid plan required`, `insufficient credits`, `asset category mismatch`, `voice asset required`, `asset locked`, `asset expired`, `provider error`, `provider timeout`, `unauthenticated`, `rate limit`, `server error`. See [error-codes.md](../../../docs/error-codes.md) for the full catalog and retry guidance.

## Official sample

### Official text-to-speech audio

- Sample ID: `sample_generate_audio_001`
- Input: `voice_asset_id=official_voice_demo_001`, `text=Welcome to Medux. This audio was generated from text.`
- Output: `output_url=Official example audio output`
- Model: `speech-standard`
- Minimum plan: `free`
- Preview: [Open documented sample](https://medux-cdn-dev.hifly.cc/demo/14bb9aadd2fb4a1c5703ac0f8cfeb1c6.mp3)

## MCP alternative

The same capability is optionally available through Medux MCP.

- MCP endpoint: `https://medux.io/mcp`
- Tool: `medux_speech_create_audio`
- Result type: `AUDIO`

Example prompt:

```text
Generate speech audio from this text using voice_asset_id {voice_asset_id} and model_id speech-standard.
```


## Related APIs

- No related endpoints documented.

## Source of truth

- [Official API Reference](https://medux.io/api-reference/generate/create-audio)
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
