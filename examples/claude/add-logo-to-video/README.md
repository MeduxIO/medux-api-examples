# How to Add a Logo Watermark to Video with Claude MCP and Medux

Use one natural-language request to let Claude inspect your media, call Medux through MCP, upload the assets, position the logo, and return a finished MP4.

## What this example does

Use one natural-language request to let Claude inspect your media, call Medux through MCP, upload the assets, position the logo, and return a finished MP4.

| Interface | Value |
| --- | --- |
| Agent | Claude |
| MCP tool | `MEDUX_SIGNED_UPLOAD_URL` |
| API endpoint | [See API reference](https://medux.io/api-reference/media/add-logo-to-video) |

## Before you run it

1. Connect Medux MCP to Claude.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Prompt used in Claude Use Medux to add logo.png to sample.mp4. Resize the logo to an appropriate size and place it in the top-right corner of the video. Upload the files using the curl command.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| — | — | — | This operation has no documented request fields. |

## Run the workflow

1. Paste the prompt into Claude.
2. Confirm that Claude selects `MEDUX_SIGNED_UPLOAD_URL`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/add_logo_to_video_claude_mcp.html)
- [API reference](https://medux.io/api-reference/media/add-logo-to-video)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
