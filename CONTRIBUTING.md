# Contributing

Thanks for helping improve the Medux examples.

## Updating generated examples

The files under `examples/`, the root `README.md`, and `examples.json` are generated from the official Medux API Reference snapshot:

```bash
python3 scripts/fetch_api_reference.py
python3 scripts/generate_examples.py
python3 scripts/validate_examples.py
```

Update the official API Reference first instead of editing generated example files by hand. The committed `api-reference.json` makes contract changes reviewable.

## Adding hand-written code

Hand-written SDK or REST examples may be added alongside an example in a language-specific subdirectory. They must:

- use environment variables for credentials;
- include an `.env.example` containing placeholders only;
- avoid committing private asset IDs, media URLs, or user data;
- document installation and execution commands;
- handle API errors and asynchronous tasks where applicable;
- link to the matching Medux API reference.

## Pull requests

Keep each pull request focused, explain how the example was tested, and run the validator before submitting it.
