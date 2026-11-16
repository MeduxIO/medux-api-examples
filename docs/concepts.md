# Core concepts

Read this once before running the examples. The per-endpoint READMEs assume the
model below and do not repeat it.

## Base URL and environments

All examples target `https://api.medux.io`. Every path in this repository is
absolute, e.g. `POST /api/app/v1/clone/avatar/by_image`.

The Python and JavaScript clients read an optional `MEDUX_API_BASE_URL`
environment variable and fall back to `https://api.medux.io` when it is unset.
Set it only to target a non-production host; `curl.sh` always uses the
production URL inline.

## Files vs. assets

- A **file** is raw uploaded bytes referenced by a `file_id`. You obtain one
  through the upload flow (see below). Most media operations take one or more
  `file_id` inputs.
- An **asset** is a persisted, reusable Medux record (for example a cloned
  avatar or voice) referenced by an `asset_id`. Assets are created by some
  operations and consumed by others.

Do not pass a local file path or a chat attachment where a `file_id` or
`asset_id` is expected; you must run the upload flow first.

## Upload flow

Most inputs must be uploaded before use:

1. Call [Create Upload URL](../examples/get-started/create-upload-url/) to get a
   pre-signed `upload_url` and a `file` reference.
2. `PUT`/`POST` the raw bytes directly to `upload_url` with the returned
   `content_type`.
3. Use the returned `file_id` in the operation you actually want to run.

## Asynchronous task lifecycle

Most `POST` operations that produce media do **not** return the finished result.
They enqueue a task and return `data.task` with a task ID. HTTP `200` only means
the task was accepted, not that processing finished.

To get a result, poll [Get Task](../examples/infra/get-task/) with the `task_id` until the
task reaches a terminal state (succeeded or failed). One endpoint covers every
domain: clone, generate, edit, video, voice and document tasks.

Poll with a backoff (for example every few seconds) rather than in a tight loop.
[Sync Task](../examples/infra/sync-task/) can force a status refresh from the
provider when a task appears stuck.

## Application response envelope

Every response carries an application-level `code` and `message` in addition to
the HTTP status. `code == 0` (`message == "ok"`) is success; any other value is
an error you must handle. Always check `code` even on HTTP `200`. The full list
is in [error-codes.md](error-codes.md).

## Pagination

List endpoints (`List Assets`, `List Tasks`, `List Results`, `List Avatars`,
`List Voices`) accept `cursor` and `limit` query parameters and return
`data.next_cursor`. Keep requesting with the returned cursor until it is empty
or absent.

## Credits and plans

Billable operations consume credits and some require a paid plan. A request can
fail with `insufficient credits` (`1401`) or `paid plan required` (`1409`), and
responses may include `data.paid_plan_required`. Each official sample documents
its `Minimum plan`. See [Pricing](https://medux.io/pricing).

## Source of truth

The [official API Reference](https://medux.io/api-reference/) is authoritative.
This repository is a generated snapshot; contracts and limits may change.
