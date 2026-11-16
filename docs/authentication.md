# Authentication and setup

## Prerequisites

- **API key** — create one from the [Medux MCP / API overview](https://medux.io/overview/mcp). The REST API always authenticates with this key as a Bearer token; OAuth sign-in is only for the MCP server (`https://medux.io/mcp`).
- **Python** 3.9 or newer (for `example.py`), with `pip`.
- **Node.js** 18 or newer (for `example.mjs`; uses built-in `fetch`).
- **curl** and **bash** (for `curl.sh`).
- **git** (to clone the repository).

## API key

All requests authenticate with a bearer token in the `Authorization` header:

```
Authorization: Bearer <MEDUX_API_KEY>
```

Never hard-code or commit a key. Provide it through the environment instead.

## Environment variables

| Variable | Required | Used by | Purpose |
| --- | --- | --- | --- |
| `MEDUX_API_KEY` | Yes | all examples | Bearer credential for every request. |
| `MEDUX_API_BASE_URL` | No | `example.py`, `example.mjs` | Overrides the API host. Defaults to `https://api.medux.io`. `curl.sh` uses the production URL inline. |
| Per-endpoint placeholders | Sometimes | `example.py`, `example.mjs` | Values such as `FILE_ID`, `TASK_ID`, `VOICE_ASSET_ID`, `CURSOR`, `LIMIT`. Each endpoint README lists the ones it needs. |

Copy [`.env.example`](../.env.example) to `.env` and fill in values, then export
them into your shell:

```bash
cp .env.example .env
# edit .env, then:
set -a && . ./.env && set +a
```

Or export directly:

```bash
export MEDUX_API_KEY="your_api_key"
```

`.env` is git-ignored; `.env.example` (placeholders only) is committed.

## Running an example

```bash
# Python
python3 -m pip install -r requirements.txt
python3 examples/<module>/<endpoint>/example.py

# JavaScript
node examples/<module>/<endpoint>/example.mjs

# curl
bash examples/<module>/<endpoint>/curl.sh
```

For curl, replace uppercase placeholders (for example `FILE_ID`) inline before
running. The Python and JavaScript clients resolve their documented placeholders
from the environment and will error clearly if a required variable is missing.

See [concepts.md](concepts.md) for the upload flow and asynchronous task model,
and [error-codes.md](error-codes.md) for response handling.
