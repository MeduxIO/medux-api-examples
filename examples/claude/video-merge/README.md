# How to Merge Video Clips with Claude MCP and Medux

This tutorial shows a streamlined workflow for combining two MP4 files. Claude identifies the Medux tools, creates upload URLs, sends the clips, starts the merge task, and returns a playable result.

## What this example does

This tutorial shows a streamlined workflow for combining two MP4 files. Claude identifies the Medux tools, creates upload URLs, sends the clips, starts the merge task, and returns a playable result.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `video_merge` |
| API endpoint | [See API reference](https://medux.io/api-reference/media/merge-video) |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Use Medux to merge two video clips: sample-clip-3s.mp4 and sample-clip-7s.mp4. Upload the files using the curl command.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `video_merge`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/video_merge_claude_mcp.html)
- [API reference](https://medux.io/api-reference/media/merge-video)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
