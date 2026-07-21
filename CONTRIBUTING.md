# Contributing

Thanks for helping improve the Medux examples.

## Prerequisites

- Python 3.9+ and Node.js 18+ (used to validate `example.py` and `example.mjs`).
- Never commit real API keys, private asset IDs, media URLs, or user data.
  Copy [`.env.example`](./.env.example) to `.env` for local runs; `.env` is
  git-ignored.

See [docs/authentication.md](./docs/authentication.md) for full setup and
[docs/concepts.md](./docs/concepts.md) for the upload and task model.

## What is generated vs. hand-maintained

Generated from the official Medux API Reference snapshot — **do not edit by hand:**

- everything under `examples/`
- the root `README.md`
- `examples.json`

Hand-maintained — edit these directly:

- `docs/`, `CONTRIBUTING.md`, `LICENSE`, `.env.example`
- `scripts/` (the generator and validator)

## Updating generated examples

Change the generator or the reference snapshot, then regenerate:

```bash
python3 scripts/fetch_api_reference.py     # refresh api-reference.json
python3 scripts/generate_examples.py       # regenerate examples/ + README.md
python3 scripts/validate_examples.py       # verify
```

To change the shape or wording of every example (sections, error tables, code
clients), edit `scripts/generate_examples.py` rather than the output. The
committed `api-reference.json` makes contract changes reviewable.

## Adding hand-written code

Hand-written SDK or REST examples may be added alongside an example in a
language-specific subdirectory. They must:

- use environment variables for credentials (never inline secrets);
- rely on the repository-level [`.env.example`](./.env.example), or add a local
  one containing placeholders only;
- avoid committing private asset IDs, media URLs, or user data;
- document installation and execution commands;
- handle API errors and asynchronous tasks where applicable
  (see [docs/error-codes.md](./docs/error-codes.md));
- link to the matching Medux API reference.

## Pull requests

Keep each pull request focused, explain how the example was tested, and run
`python3 scripts/validate_examples.py` before submitting it.
