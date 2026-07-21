# Response codes

Every Medux response includes an application-level `code` (and a matching
`message`) independent of the HTTP status. `0` is success; treat any other value
as an error, even when the HTTP status is `200`.

```json
{ "code": 0, "message": "ok", "data": { } }
```

## Canonical codes

This table is the consolidated, normalized reference for the whole API. The
per-endpoint response tables list only the subset each endpoint can return, so
use this page as the authoritative catalog.

| Code | Message | Meaning |
| --- | --- | --- |
| `0` | `ok` | Success. |
| `12` | `invalid input` | The request was rejected as malformed or invalid. |
| `13` | `unauthenticated` | Authentication is required or the credential is invalid. |
| `15` | — | Resource not found. |
| `16` | `rate limit` | Rate limit exceeded; retry after backing off. |
| `99` | `server error` | Unexpected server error. |
| `1401` | `insufficient credits` | The account does not have enough credits. |
| `1402` | `asset category mismatch` | The asset category does not match this operation. |
| `1403` | — | A voice asset is required for this operation. |
| `1404` | `provider error` | The upstream provider returned an error. |
| `1405` | `provider timeout` | The upstream provider request timed out. |
| `1409` | `paid plan required` | The capability requires a paid plan; see `data.paid_plan_required`. |
| `1410` | `invalid model` | The requested `model_id` is invalid or unavailable. |

### Reserved media-domain range

Codes in the range `1401`–`1499` are media-domain errors. Some values that
appear in individual endpoint `enum` lists are **not yet described in the public
reference**:

| Code | Status |
| --- | --- |
| `1406` | Meaning not published in the official reference. |
| `1407` | Meaning not published in the official reference. |
| `1408` | Meaning not published in the official reference. |

If you receive one of these, rely on the accompanying `message` field and treat
it as a non-retryable media error unless the message says otherwise. Please open
an issue if you observe a stable meaning so this table can be completed.

## Handling guidance

- Check `code` before consuming `data`, on every response.
- Retry only `16` (rate limit) and `1405` (provider timeout), with backoff.
- Do not retry `12`, `13`, `1401`, `1402`, `1403`, `1409`, or `1410`; fix the
  request, credential, plan, or inputs first.
- For asynchronous operations, a success envelope means the task was
  *accepted*. Poll the task-status endpoint for the real outcome — see
  [concepts.md](concepts.md#asynchronous-task-lifecycle).

The [official API Reference](https://medux.io/api-reference/) is the source of
truth; this catalog is derived from the committed `api-reference.json` snapshot.
