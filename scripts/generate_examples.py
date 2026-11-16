#!/usr/bin/env python3
"""Generate API-first examples from the official Medux API Reference snapshot."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import urllib.parse
from collections import defaultdict
from pathlib import Path


API_BASE_URL = "https://api.medux.io"
PLACEHOLDER_RE = re.compile(r"^[A-Z][A-Z0-9_]{2,}$")
UNAVAILABLE_PREVIEWS: set[str] = set()
# Canonical, normalized meanings for the application-level response `code`.
# The reference publishes these inconsistently (a markdown table for some
# endpoints, a "\.. N: msg" list for others, occasionally with untranslated
# text). We render a uniform list from this map and point to docs/error-codes.md
# for the full catalog. Codes with no published meaning are labelled explicitly.
CODE_MEANINGS = {
    "0": "OK",
    "12": "Invalid input",
    "13": "Authentication is required",
    "15": "Resource not found",
    "16": "Rate limit exceeded",
    "99": "Server error",
    "1401": "Insufficient credits",
    "1402": "Asset category does not match this operation",
    "1403": "Voice asset is required",
    "1404": "Provider returned an error",
    "1405": "Provider request timed out",
    "1409": "Paid plan required",
    "1410": "Invalid model",
}
CODE_UNDOCUMENTED = "Reserved media-domain error; meaning not published in the reference."
ERROR_CODES_DOC = "../../../docs/error-codes.md"
# Detects raw, non-prose descriptions leaked from the reference: dotted-enum
# bullets ("... enums:", "..... ACTIVE") and protobuf type names.
MALFORMED_DESC_RE = re.compile(r"\.\.+ |enums:|[a-z]+hpb\.")
FIELD_DESCRIPTIONS = {
    "audio_file_id": "Identifier of the uploaded audio file used by this operation.",
    "capability_id": "Filter records by Medux capability identifier.",
    "cursor": "Opaque pagination cursor returned by the previous page.",
    "emotion": "Voice emotion adjustment value.",
    "file_id": "Identifier of a file created through the Medux upload flow.",
    "limit": "Maximum number of records to return in this page.",
    "media_type": "Media-type filter for the returned records.",
    "project_id": "Identifier of the Medux project used to create the output.",
    "prompt": "Natural-language instruction describing the requested output.",
    "region.height": "Height of the target processing region.",
    "region.width": "Width of the target processing region.",
    "speed": "Voice or media speed adjustment value.",
    "status": "Filter records by lifecycle status.",
    "storage_object.key": "Storage object key returned by the upload flow.",
    "storage_object.url": "Storage object URL associated with the uploaded file.",
    "task_id": "Identifier of the Medux task to retrieve or synchronize.",
    "text": "Text content used to generate speech or media.",
    "title": "Optional user-facing title for the task or generated asset.",
    "tone": "Voice tone adjustment value.",
    "voice_asset_id": "Identifier of the reusable Medux voice asset.",
    "data.asset": "Asset created or returned by the operation when available.",
    "data.entitlement": "Plan or entitlement information relevant to the request.",
    "data.items": "Collection of records returned by a list operation.",
    "data.next_cursor": "Opaque cursor to request the next page; absent or empty when no next page is available.",
    "data.paid_plan_required": "Paid-plan requirement details when the selected capability is unavailable on the current plan.",
    "data.retention_notice": "Retention-policy information associated with the returned data.",
    "data.task": "Task record created or returned by an asynchronous operation.",
    "message": "Human-readable application status or error message.",
}


KNOWN_ENDPOINTS: set[tuple[str, str]] = set()
# Old example path -> current path, from legacy-paths.json. Old paths keep a short
# redirect README so existing links and search results do not dead-end.
LEGACY_PATHS: dict[str, str] = {}
LEGACY_NOTES: dict[str, str] = {}


def md(value: object) -> str:
    if value is None or value == "":
        return "—"
    return str(value).replace("\\\n", "\n").replace("|", "\\|").replace("\n", "<br>")


def code_details(enum_values: list[str]) -> str:
    """Render a uniform, complete meaning list for the response `code` field."""
    lines = [
        f"Application response code. Full catalog: [error-codes.md]({ERROR_CODES_DOC}).",
    ]
    for value in enum_values:
        meaning = CODE_MEANINGS.get(value, CODE_UNDOCUMENTED)
        lines.append(f"- `{value}` — {meaning}")
    return "\n".join(lines)


def field_rows(fields: list[dict]) -> str:
    if not fields:
        return "| — | — | — | — | No fields documented. |"
    rows = []
    for field in fields:
        if field.get("name") == "code" and field.get("enum_values"):
            details = code_details(field["enum_values"])
        else:
            raw = field.get("description") or ""
            if not raw or MALFORMED_DESC_RE.search(raw):
                # Reference sometimes leaks raw proto/dotted-enum text; fall back
                # to a curated description and let the Options line carry values.
                details = FIELD_DESCRIPTIONS.get(field.get("name"), "No additional description is documented.")
            else:
                details = raw
            if field.get("enum_values"):
                details += "\nOptions: " + ", ".join(f"`{value}`" for value in field["enum_values"])
        rows.append(
            "| `{name}` | `{type}` | {required} | `{location}` | {details} |".format(
                name=md(field.get("name")),
                type=md(field.get("type")),
                required="Required" if field.get("required") else "Optional",
                location=md(field.get("location")),
                details=md(details),
            )
        )
    return "\n".join(rows)


def executable_curl(command: str) -> str:
    command = command.replace(
        "-H 'Authorization: Bearer $MEDUX_API_KEY'",
        '-H "Authorization: Bearer $MEDUX_API_KEY"',
    )
    return re.sub(
        r"https://[^\s\\]+",
        lambda match: f"'{match.group(0)}'" if "?" in match.group(0) else match.group(0),
        command,
        count=1,
    )


def curl_body(command: str) -> object | None:
    match = re.search(r"(?:^|\s)-d\s+'([^']+)'", command, re.S)
    return json.loads(match.group(1)) if match else None


def request_placeholders(value: object, fields_by_name: dict[str, dict], prefix: str = "") -> set[str]:
    placeholders: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            name = f"{prefix}.{key}" if prefix else key
            placeholders.update(request_placeholders(child, fields_by_name, name))
    elif isinstance(value, list):
        for child in value:
            placeholders.update(request_placeholders(child, fields_by_name, prefix))
    elif isinstance(value, str) and PLACEHOLDER_RE.fullmatch(value):
        field = fields_by_name.get(prefix, {})
        if value not in field.get("enum_values", []):
            placeholders.add(value)
    return placeholders


def endpoint_placeholders(page: dict, body: object | None) -> list[str]:
    fields = page["request_section"].get("fields", [])
    fields_by_name = {field["name"]: field for field in fields}
    values = request_placeholders(body, fields_by_name) if body is not None else set()
    for field in fields:
        if field.get("location") == "PATH":
            values.add(field["name"].upper())
    return sorted(values)


def render_python(page: dict, body: object | None) -> str:
    summary = page["endpoint_summary"]
    fields = page["request_section"].get("fields", [])
    path_fields = [field for field in fields if field.get("location") == "PATH"]
    query_fields = [field for field in fields if field.get("location") == "QUERY"]
    fields_by_name = {field["name"]: field for field in fields}
    body_placeholders = sorted(request_placeholders(body, fields_by_name)) if body is not None else []
    lines = [
        '"""Runnable example generated from the official Medux API Reference."""',
        "",
        "import json",
        "import os",
        "",
        "import requests",
        "",
        f'BASE_URL = os.getenv("MEDUX_API_BASE_URL", "{API_BASE_URL}")',
        f"PLACEHOLDERS = frozenset({body_placeholders!r})",
        "",
        "",
        "def require_env(name: str) -> str:",
        "    value = os.getenv(name)",
        "    if not value:",
        '        raise RuntimeError(f"Set {name} before running this example")',
        "    return value",
        "",
        "",
        "def resolve_placeholders(value):",
        "    if isinstance(value, dict):",
        "        return {key: resolve_placeholders(item) for key, item in value.items()}",
        "    if isinstance(value, list):",
        "        return [resolve_placeholders(item) for item in value]",
        "    if isinstance(value, str) and value in PLACEHOLDERS:",
        "        return require_env(value)",
        "    return value",
        "",
        "",
        f'path = "{summary["path"]}"',
    ]
    for field in path_fields:
        lines.append(f'path = path.replace("{{{field["name"]}}}", require_env("{field["name"].upper()}"))')
    lines.extend(["url = f\"{BASE_URL}{path}\"", ""])
    if query_fields:
        lines.extend(["params = {}"])
        for field in query_fields:
            env_name = field["name"].upper()
            lines.extend(
                [
                    f'if os.getenv("{env_name}"):',
                    f'    params["{field["name"]}"] = os.environ["{env_name}"]',
                ]
            )
        lines.append("")
    if body is not None:
        encoded = json.dumps(body, indent=2, ensure_ascii=False)
        lines.extend(
            [
                "payload = resolve_placeholders(json.loads(r'''",
                encoded,
                "'''))",
                "",
            ]
        )
    call = [
        f'    "{summary["method"]}",',
        "    url,",
        '    headers={"Authorization": f"Bearer {require_env(\'MEDUX_API_KEY\')}"},',
    ]
    if query_fields:
        call.append("    params=params,")
    if body is not None:
        call.append("    json=payload,")
    call.extend(["    timeout=120,", ")"])
    lines.extend(
        [
            "response = requests.request(",
            *call,
            "response.raise_for_status()",
            "result = response.json()",
            'if result.get("code") not in (None, 0):',
            '    raise RuntimeError(f"Medux API error: {result.get(\'code\')} {result.get(\'message\')}")',
            "print(json.dumps(result, indent=2))",
            "",
        ]
    )
    return "\n".join(lines)


def render_javascript(page: dict, body: object | None) -> str:
    summary = page["endpoint_summary"]
    fields = page["request_section"].get("fields", [])
    path_fields = [field for field in fields if field.get("location") == "PATH"]
    query_fields = [field for field in fields if field.get("location") == "QUERY"]
    fields_by_name = {field["name"]: field for field in fields}
    body_placeholders = sorted(request_placeholders(body, fields_by_name)) if body is not None else []
    lines = [
        "/** Runnable example generated from the official Medux API Reference. */",
        "",
        f'const baseUrl = process.env.MEDUX_API_BASE_URL ?? "{API_BASE_URL}";',
        f"const placeholders = new Set({json.dumps(body_placeholders)});",
        "",
        "function requireEnv(name) {",
        "  const value = process.env[name];",
        '  if (!value) throw new Error(`Set ${name} before running this example`);',
        "  return value;",
        "}",
        "",
        "function resolvePlaceholders(value) {",
        "  if (Array.isArray(value)) return value.map(resolvePlaceholders);",
        "  if (value && typeof value === \"object\") {",
        "    return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, resolvePlaceholders(item)]));",
        "  }",
        '  if (typeof value === "string" && placeholders.has(value)) return requireEnv(value);',
        "  return value;",
        "}",
        "",
        f'let path = "{summary["path"]}";',
    ]
    for field in path_fields:
        lines.append(f'path = path.replace("{{{field["name"]}}}", encodeURIComponent(requireEnv("{field["name"].upper()}")));')
    lines.extend(["const url = new URL(path, baseUrl);", ""])
    for field in query_fields:
        env_name = field["name"].upper()
        lines.append(f'if (process.env.{env_name}) url.searchParams.set("{field["name"]}", process.env.{env_name});')
    if query_fields:
        lines.append("")
    if body is not None:
        encoded = json.dumps(body, indent=2, ensure_ascii=False)
        lines.extend([f"const payload = resolvePlaceholders({encoded});", ""])
    lines.extend(
        [
            "const response = await fetch(url, {",
            f'  method: "{summary["method"]}",',
            "  headers: {",
            '    Authorization: `Bearer ${requireEnv("MEDUX_API_KEY")}`,',
        ]
    )
    if body is not None:
        lines.append('    "Content-Type": "application/json",')
    lines.extend(["  },"])
    if body is not None:
        lines.append("  body: JSON.stringify(payload),")
    lines.extend(
        [
            "});",
            "",
            "const result = await response.json();",
            "if (!response.ok) {",
            "  throw new Error(`${response.status} ${JSON.stringify(result)}`);",
            "}",
            "if (result.code !== undefined && result.code !== 0) {",
            "  throw new Error(`Medux API error: ${result.code} ${result.message ?? \"\"}`);",
            "}",
            "console.log(JSON.stringify(result, null, 2));",
            "",
        ]
    )
    return "\n".join(lines)


def render_samples(samples: list[dict]) -> str:
    if not samples:
        return "No official media sample is currently documented for this endpoint."
    blocks = []
    for sample in samples:
        input_fields = ", ".join(f"`{field['key']}={field['value']}`" for field in sample.get("sample_input", {}).get("fields", [])) or "—"
        output_fields = ", ".join(f"`{field['key']}={field['value']}`" for field in sample.get("sample_output", {}).get("fields", [])) or "—"
        preview = sample.get("sample_output", {}).get("preview_url")
        if preview in UNAVAILABLE_PREVIEWS:
            preview_line = "- Preview: currently unavailable; the URL published by the official reference returned HTTP 404 during validation. The original URL remains in `reference.json`."
        elif preview:
            preview_line = f"- Preview: [Open documented sample]({preview})"
        else:
            preview_line = "- Preview: —"
        blocks.extend(
            [
                f"### {sample.get('title', sample.get('sample_id', 'Official sample'))}",
                "",
                f"- Sample ID: `{sample.get('sample_id', '—')}`",
                f"- Input: {input_fields}",
                f"- Output: {output_fields}",
                f"- Model: `{sample.get('model_id', '—')}`",
                f"- Minimum plan: `{sample.get('minimum_plan', '—')}`",
                preview_line,
            ]
        )
    return "\n".join(blocks)


def render_mcp(page: dict) -> str:
    tool = page.get("mcp_tool")
    if not tool:
        return "This endpoint does not currently document a hosted MCP tool."
    prompt = ""
    samples = tool.get("prompt_samples") or []
    if samples:
        prompt = f"""

Example prompt:

```text
{samples[0].get('natural_language_prompt', '')}
```"""
    return f"""The same capability is optionally available through Medux MCP.

- MCP endpoint: `https://medux.io/mcp`
- Tool: `{tool.get('mcp_tool_id', '—')}`
- Result type: `{samples[0].get('expected_result_type', '—') if samples else '—'}`{prompt}
"""


def render_readme(page: dict, body: object | None, curl_command: str) -> str:
    meta = page["meta"]
    summary = page["endpoint_summary"]
    request_fields = page["request_section"].get("fields", [])
    response_fields = page["response_section"].get("fields", [])
    auth_items = "\n".join(f"- {item}" for item in page.get("auth_requirements", {}).get("items", [])) or "- No authentication requirement documented."
    preconditions = "\n".join(f"- {item}" for item in page.get("preconditions", {}).get("items", [])) or "- No additional preconditions documented."
    placeholders = endpoint_placeholders(page, body)
    env_lines = ["- `MEDUX_API_KEY` — required for every request."]
    env_lines.extend(f"- `{name}` — replace the corresponding placeholder in the official example." for name in placeholders)
    path_fields = [field for field in request_fields if field.get("location") == "PATH"]
    query_fields = [field for field in request_fields if field.get("location") == "QUERY"]
    env_lines.extend(f"- `{field['name'].upper()}` — path parameter `{field['name']}`." for field in path_fields if field["name"].upper() not in placeholders)
    env_lines.extend(f"- `{field['name'].upper()}` — optional query parameter `{field['name']}`." for field in query_fields)
    related = []
    for link in page.get("related_links", []):
        module = link.get("module")
        slug = link.get("endpoint_slug")
        if module and slug and (module, slug) in KNOWN_ENDPOINTS:
            related.append(f"- [{link['title']}](../../{module}/{slug}/) — {link.get('description', '')}")
    related_text = "\n".join(related) or "- No related endpoints documented."
    module = meta["module"]
    # Every asynchronous endpoint is polled through the single Get Task endpoint.
    status_target = "../../infra/get-task/"
    if any(field.get("name") == "data.task" for field in response_fields):
        status_link = f"the [relevant task-status endpoint]({status_target})" if status_target else "the relevant task-status endpoint"
        task_note = f"This response can include `data.task`. Persist the returned task ID and use {status_link} until the task reaches a terminal state. Do not treat HTTP 200 alone as proof that asynchronous media processing has completed."
    else:
        task_note = "Check both the HTTP status and the application-level `code` and `message` fields before consuming `data`."
    message_field = next((field for field in response_fields if field.get("name") == "message"), {})
    errors = [value for value in message_field.get("enum_values", []) if value != "ok"]
    error_note = ", ".join(f"`{value}`" for value in errors) or "the non-success values documented above"
    return f"""# {meta['title']}

{page.get('hero', {}).get('summary') or meta.get('summary') or summary.get('summary')}

## Endpoint

```http
{summary['method']} {summary['path']}
```

Base URL: `{API_BASE_URL}`

{summary.get('summary', '')}

## Authentication

{auth_items}

Export your credential before running an example:

```bash
export MEDUX_API_KEY="your_api_key"
```

Never commit a real key.

## Preconditions

{preconditions}

## Request

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
{field_rows(request_fields)}

## Environment variables used by the Python and JavaScript examples

{chr(10).join(dict.fromkeys(env_lines))}

Query parameters are only sent by the Python and JavaScript examples when their corresponding environment variables are set.

## curl

```bash
{curl_command}
```

The same command is available in [`curl.sh`](./curl.sh).

The curl form mirrors the official reference. Replace uppercase placeholders such as `FILE_ID`, `TASK_ID`, or `MODEL_ID` inline before running it; the Python and JavaScript examples resolve their documented placeholders from environment variables.

## Python

Install the dependency and run:

```bash
python3 -m pip install -r ../../../requirements.txt
python3 example.py
```

See [`example.py`](./example.py).

## JavaScript

Node.js 18 or newer is required:

```bash
node example.mjs
```

See [`example.mjs`](./example.mjs).

## Response

| Field | Type | Requirement | Location | Description / options |
| --- | --- | --- | --- | --- |
{field_rows(response_fields)}

### Response handling

{task_note}

The response-field table above lists the `code` values this endpoint can return, each with its meaning. Handle the documented non-success messages explicitly: {error_note}. See [error-codes.md]({ERROR_CODES_DOC}) for the full catalog and retry guidance.

## Official sample

{render_samples(page.get('examples', {}).get('samples', []))}

## MCP alternative

{render_mcp(page)}

## Related APIs

{related_text}

## Source of truth

- [Official API Reference]({page['source_url']})
- [Medux API quick start](https://medux.io/overview/api)
- [Medux tutorials](https://medux.io/tutorials/)

This repository snapshot is generated from the official API Reference. Re-check the linked reference before production deployment because contracts and limits may change.
"""


def render_root(snapshot: dict) -> str:
    groups: dict[str, list[dict]] = defaultdict(list)
    for page in snapshot["endpoints"]:
        groups[page["meta"]["module"]].append(page)
    sections = []
    titles = {group["slug"]: group["title"] for group in snapshot.get("groups", [])}
    for module, pages in groups.items():
        lines = [f"### {titles.get(module, module.title())}", "", "| API | Method | Endpoint |", "| --- | --- | --- |"]
        for page in pages:
            meta = page["meta"]
            summary = page["endpoint_summary"]
            lines.append(f"| [{meta['title']}](./examples/{module}/{meta['endpoint_slug']}/) | `{summary['method']}` | `{summary['path']}` |")
        sections.append("\n".join(lines))
    legacy_table = "\n".join(
        f"| `examples/{old}/` | [`examples/{new}/`](./examples/{new}/) |" for old, new in sorted(LEGACY_PATHS.items())
    )
    return f"""# Medux API Examples

Complete API-first examples generated from the [official Medux API Reference](https://medux.io/api-reference/).

The REST API does not differ between Claude, Codex, or other clients. Each of the **{snapshot['endpoint_count']} APIs** has one canonical example containing its contract, curl command, runnable Python and JavaScript clients, response handling, official sample data, and optional MCP mapping.

The same capabilities are also exposed as MCP tools at `https://medux.io/mcp` (OAuth or API key). See the [MCP tool reference](https://github.com/MeduxIO/medux-mcp-examples/blob/main/docs/tools.md) and [Connect Medux MCP](https://github.com/MeduxIO/medux-mcp-examples/blob/main/docs/connection.md).

## Prerequisites

- A Medux API key — see [docs/authentication.md](./docs/authentication.md).
- Python 3.9+ (for `example.py`) and/or Node.js 18+ (for `example.mjs`).
- `curl` and `bash` (for `curl.sh`).

New to the API? Read [docs/concepts.md](./docs/concepts.md) first: it covers the
upload flow, the asynchronous task lifecycle, credits, and pagination that the
per-endpoint pages assume.

## Quick start

```bash
git clone https://github.com/MeduxIO/medux-api-examples.git
cd medux-api-examples
cp .env.example .env            # then edit .env with your key
export MEDUX_API_KEY="your_api_key"
python3 -m pip install -r requirements.txt
```

Choose an API below. For Python and JavaScript, set the placeholder environment variables documented in its README; set `MEDUX_API_BASE_URL` only to target a non-production host. For curl, replace the uppercase placeholders inline before running `curl.sh`.

## API catalog

{chr(10).join(chr(10) + section for section in sections)}

## Repository layout

```text
examples/<module>/<endpoint>/
├── README.md       # Complete endpoint guide
├── curl.sh         # Copy-ready official curl request
├── example.py      # Python client
├── example.mjs     # Node.js client
├── request.json    # Official request body example
└── reference.json  # Structured endpoint reference
```

## Moved examples

Some examples moved when the official API Reference was reorganized. Each old path
still contains a short README that points to the current page.

| Old path | Current page |
| --- | --- |
{legacy_table}
## Refreshing from the official reference

```bash
python3 scripts/fetch_api_reference.py
python3 scripts/generate_examples.py
python3 scripts/validate_examples.py
```

The committed `api-reference.json` is a reviewable snapshot of the public reference used to generate the repository.

## Documentation

- [docs/authentication.md](./docs/authentication.md) — prerequisites, API key, and environment variables.
- [docs/concepts.md](./docs/concepts.md) — files vs. assets, upload flow, async task lifecycle, credits, and pagination.
- [docs/error-codes.md](./docs/error-codes.md) — the consolidated response-code catalog and retry guidance.

## Security

Never commit API keys, private asset IDs, private media URLs, or user data. Store credentials in environment variables and review requests before sending them.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1] / "api-reference.json")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    repo = args.repo.resolve()
    snapshot = json.loads(args.source.resolve().read_text(encoding="utf-8"))
    unavailable_file = repo / "unavailable-sample-previews.json"
    if unavailable_file.exists():
        unavailable = json.loads(unavailable_file.read_text(encoding="utf-8"))
        UNAVAILABLE_PREVIEWS.update(unavailable.get("urls", []))

    notes_file = repo / "legacy-notes.json"
    if notes_file.exists():
        LEGACY_NOTES.update(json.loads(notes_file.read_text(encoding="utf-8")))
    legacy_file = repo / "legacy-paths.json"
    if legacy_file.exists():
        LEGACY_PATHS.update(json.loads(legacy_file.read_text(encoding="utf-8")))

    # Related links that point at pages the site no longer publishes are dropped.
    KNOWN_ENDPOINTS.update((e["meta"]["module"], e["meta"]["endpoint_slug"]) for e in snapshot["endpoints"])

    examples_root = repo / "examples"
    if examples_root.exists():
        shutil.rmtree(examples_root)

    index = []
    for page in snapshot["endpoints"]:
        meta = page["meta"]
        target = examples_root / meta["module"] / meta["endpoint_slug"]
        target.mkdir(parents=True, exist_ok=True)
        official_curl = page["examples"]["curl_command"]
        curl_command = executable_curl(official_curl)
        body = curl_body(official_curl)
        (target / "README.md").write_text(render_readme(page, body, curl_command), encoding="utf-8")
        curl_path = target / "curl.sh"
        curl_path.write_text(
            "#!/usr/bin/env bash\nset -euo pipefail\n: \"${MEDUX_API_KEY:?Set MEDUX_API_KEY}\"\n\n" + curl_command + "\n",
            encoding="utf-8",
        )
        curl_path.chmod(0o755)
        (target / "example.py").write_text(render_python(page, body), encoding="utf-8")
        (target / "example.mjs").write_text(render_javascript(page, body), encoding="utf-8")
        (target / "request.json").write_text(json.dumps(body or {}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        (target / "reference.json").write_text(json.dumps(page, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        index.append(
            {
                "module": meta["module"],
                "slug": meta["endpoint_slug"],
                "title": meta["title"],
                "method": page["endpoint_summary"]["method"],
                "path": page["endpoint_summary"]["path"],
                "source_url": page["source_url"],
            }
        )

    for old, new in LEGACY_PATHS.items():
        stub = examples_root / old
        stub.mkdir(parents=True, exist_ok=True)
        relative = "../" * (old.count("/") + 1) + new + "/"
        (stub / "README.md").write_text(
            f"# Moved: `examples/{old}`\n\n"
            "This example moved, or its page was replaced, when the official Medux API Reference was reorganized.\n\n"
            f"Current page: [`examples/{new}/`]({relative})\n\n"
            + (f"> **Note:** {LEGACY_NOTES[old]}\n\n" if old in LEGACY_NOTES else "")
            + "See [Moved examples](../../../README.md#moved-examples) in the repository README for the full list.\n",
            encoding="utf-8",
        )
    (repo / "examples.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (repo / "README.md").write_text(render_root(snapshot), encoding="utf-8")
    print(f"Generated {len(index)} API examples")


if __name__ == "__main__":
    main()
