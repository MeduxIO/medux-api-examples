# How to Add a Logo Watermark to Video with Codex MCP and Medux

This guide turns the screen-recorded workflow into a clean, publish-ready tutorial. Codex reads the request, locates the input video and logo, calls Medux through MCP, and returns a new MP4 with the logo placed in the top-right corner.

## What this example does

This guide turns the screen-recorded workflow into a clean, publish-ready tutorial. Codex reads the request, locates the input video and logo, calls Medux through MCP, and returns a new MP4 with the logo placed in the top-right corner.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `add_logo_to_video` |
| API endpoint | `POST /api/app/v1/process/video/add_logo_to_video` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Use Medux to add logo2.png to sample.mp4. Resize the logo to an appropriate size and place it in the top-right corner of the video.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `add_logo_to_video`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/add_logo_codex_mcp.html)
- [API reference](https://medux.io/api-reference/media/add-logo-to-video)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
