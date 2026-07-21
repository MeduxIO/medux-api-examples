# How to Merge Videos with Codex MCP and Medux

Turn two local MP4 clips into one finished video without leaving Codex. Codex coordinates the workflow through MCP, while Medux handles the upload, merge, processing, and result delivery.

## What this example does

Turn two local MP4 clips into one finished video without leaving Codex. Codex coordinates the workflow through MCP, while Medux handles the upload, merge, processing, and result delivery.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `video_editing` |
| API endpoint | [See API reference](https://medux.io/api-reference/media/merge-video) |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Use Medux to merge two video clips: sample-clip-3s.mp4 and sample-clip-7s.mp4.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `video_editing`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/video_editing_codex_mcp.html)
- [API reference](https://medux.io/api-reference/media/merge-video)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
