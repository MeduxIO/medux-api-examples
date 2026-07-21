# How to Add an Audio Track to Video with Claude MCP and Medux

Use a single natural-language request in Claude to upload a silent video and an audio file, call the Medux media tool through MCP, monitor the job, and download a finished MP4 with its new audio track.

## What this example does

Use a single natural-language request in Claude to upload a silent video and an audio file, call the Medux media tool through MCP, monitor the job, and download a finished MP4 with its new audio track.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `medux_add_audio_to_video` |
| API endpoint | [See API reference](https://medux.io/api-reference/media/add-audio-to-video) |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Using Medux, add sample-audio.m4a to sample-video-no-audio.mp4. Upload both files with the curl command.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `medux_add_audio_to_video`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/add_audio_track_to_video_claude_mcp.html)
- [API reference](https://medux.io/api-reference/media/add-audio-to-video)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
