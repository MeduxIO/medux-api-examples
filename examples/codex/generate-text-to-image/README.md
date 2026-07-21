# How to Create Text to Image with Codex MCP and Medux

Learn how to use Codex MCP and Medux to generate an image from a text prompt, including setup, request fields, tool approval, and results.

## What this example does

Generate an image from a text prompt.

| Interface | Value |
| --- | --- |
| Agent | Codex |
| MCP tool | `medux_text_to_image` |
| API endpoint | `POST /api/app/v1/generate/image/text_to_image` |

## Before you run it

1. Connect Medux MCP to Codex.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
Generate an image from a text prompt.
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
| `prompt` | `string` | Required | Prompt text used to generate the image. |
| `negative_prompt` | `string` | Optional | Optional negative prompt. |
| `height` | `integer` | Optional | Output image height. Default: 1024. |
| `width` | `integer` | Optional | Output image width. Default: 1024. |
| `seed` | `integer` | Optional | Random seed. Use -1 to auto-generate. Default: -1. |
| `num_inference_steps` | `integer` | Optional | Number of inference steps. Default: 9. |
| `guidance_scale` | `number` | Optional | Guidance scale. Default: 0.0. |
| `cfg_normalization` | `boolean` | Optional | Whether to enable CFG normalization. Default: false. |
| `cfg_truncation` | `number` | Optional | CFG truncation value. Default: 1.0. |
| `max_sequence_length` | `integer` | Optional | Maximum text sequence length. Default: 512. |
| `model_id` | `string` | Optional | Text-to-image model id. Default: text-to-image-default. |
| `title` | `string` | Optional | Optional task title. |

## Run the workflow

1. Paste the prompt into Codex.
2. Confirm that Codex selects `medux_text_to_image`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial](https://medux.io/tutorials/generate_text_to_image_codex_mcp.html)
- [API reference](https://medux.io/api-reference/generate/text-to-image)
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
