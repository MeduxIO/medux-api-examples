# How to Remove Video Subtitles with Codex MCP and Medux

This guide turns the recorded workflow into a clean, publish-ready tutorial: Codex uploads a local video, calls Medux through MCP, waits for processing, and saves a subtitle-free MP4 back into the workspace.

## What this example does

This guide turns the recorded workflow into a clean, publish-ready tutorial: Codex uploads a local video, calls Medux through MCP, waits for processing, and saves a subtitle-free MP4 back into the workspace.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_signed_upload_url` |
| API endpoint | [See API reference](https://medux.io/api-reference/process/create-video-subtitle-removal) |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
/Users/chuan/projects/test_mudex/remove_subtitle.mp4
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_signed_upload_url`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/remove_subtitle_codex_mcp.html)
- [API reference](https://medux.io/api-reference/process/create-video-subtitle-removal)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
