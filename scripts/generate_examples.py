#!/usr/bin/env python3
"""Generate GitHub examples from the canonical Medux tutorial HTML files."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import defaultdict
from pathlib import Path


TAG_RE = re.compile(r"<[^>]+>")


def clean(value: str) -> str:
    value = TAG_RE.sub("", value)
    return " ".join(html.unescape(value).split())


def capture(source: str, pattern: str, *, required: bool = True) -> str:
    match = re.search(pattern, source, re.I | re.S)
    if not match:
        if required:
            raise ValueError(f"Missing expected pattern: {pattern}")
        return ""
    return clean(match.group(1))


def parse_fields(source: str) -> list[dict[str, str]]:
    section = re.search(
        r"<h2>Request fields to review</h2>.*?<tbody>(.*?)</tbody>",
        source,
        re.I | re.S,
    )
    if not section:
        return []
    fields = []
    for row in re.findall(r"<tr>(.*?)</tr>", section.group(1), re.I | re.S):
        cells = [clean(cell) for cell in re.findall(r"<td>(.*?)</td>", row, re.I | re.S)]
        if len(cells) == 4:
            fields.append(dict(zip(("name", "type", "requirement", "purpose"), cells)))
    return fields


def parse_tutorial(path: Path) -> dict:
    source = path.read_text(encoding="utf-8")
    filename = path.name
    agent = capture(source, r'<meta\s+name="medux-agent"\s+content="([^"]+)"', required=False)
    if not agent:
        agent_match = re.search(r"_(claude|codex)_mcp$", path.stem, re.I)
        if not agent_match:
            raise ValueError(f"Cannot infer agent from {path}")
        agent = agent_match.group(1).title()
    slug = re.sub(r"_(?:claude|codex)_mcp$", "", path.stem).replace("_", "-")
    prompt = capture(
        source,
        rf"<h2>Prompt\s+{re.escape(agent)}</h2>.*?<pre><code>(.*?)</code></pre>",
        required=False,
    )
    if not prompt:
        prompt = capture(source, r"<pre><code>(.*?)</code></pre>")

    category = capture(source, r'<span class="eyebrow">[^<]*?·\s*([^<]+)</span>', required=False)
    if not category:
        prefix = path.stem.split("_", 1)[0]
        category = prefix if prefix in {"clone", "document", "edit", "generate", "infra", "media", "process"} else "media"

    mcp_tool = capture(source, r'<strong>MCP tool</strong><br\s*/?>\s*<code>(.*?)</code>', required=False)
    if not mcp_tool:
        plain_source = clean(source)
        tools = re.findall(r"\b(medux_[a-z0-9_]+)\b", plain_source, re.I)
        ignored = {"medux_task_query", "medux_create_upload_url", "medux_upload_url"}
        mcp_tool = next((tool for tool in tools if tool.lower() not in ignored), tools[0] if tools else "")
    if not mcp_tool:
        tool_match = re.search(r'["\']?tool["\']?\s*:\s*["\']([a-z0-9_]+)', plain_source, re.I)
        if tool_match:
            mcp_tool = tool_match.group(1)
    if not mcp_tool:
        mcp_tool = slug.replace("-", "_")

    endpoint = capture(source, r'<span class="method">.*?</span>\s*<code>(.*?)</code>', required=False)
    method = capture(source, r'<span class="method">(.*?)</span>', required=False)
    if not endpoint:
        endpoint_match = re.search(r"\b(GET|POST|PUT|PATCH|DELETE)\s+(/api/[A-Za-z0-9_{}?&=./:-]+)", clean(source))
        if endpoint_match:
            method, endpoint = endpoint_match.groups()

    api_reference_url = capture(source, r'<a\s+class="api-link"\s+href="([^"]+)"', required=False)
    if not api_reference_url:
        links = re.findall(r'href="(https://medux\.io/api-reference/[^"]+)"', source, re.I)
        if not links:
            raise ValueError(f"Cannot find API reference in {path}")
        api_reference_url = html.unescape(links[0])

    title = capture(source, r'<h1[^>]*id="page-title"[^>]*>(.*?)</h1>')
    description = capture(source, r'<p class="lead">(.*?)</p>')
    operation = capture(source, r'<h2>What this tutorial does</h2>.*?<strong>Medux operation</strong><p>(.*?)</p>', required=False)
    if not operation:
        operation = description
    return {
        "id": path.stem,
        "slug": slug,
        "agent": agent.lower(),
        "category": category.lower(),
        "title": title,
        "description": description,
        "operation": operation,
        "method": method,
        "endpoint": endpoint,
        "mcp_tool": mcp_tool,
        "prompt": prompt,
        "tutorial_url": capture(source, r'<link\s+rel="canonical"\s+href="([^"]+)"'),
        "api_reference_url": api_reference_url,
        "fields": parse_fields(source),
        "source_file": filename,
    }


def render_example(item: dict) -> str:
    field_rows = "\n".join(
        f"| `{field['name']}` | `{field['type']}` | {field['requirement']} | {field['purpose']} |"
        for field in item["fields"]
    )
    if not field_rows:
        field_rows = "| — | — | — | This operation has no documented request fields. |"
    agent_name = item["agent"].title()
    endpoint_value = f"`{item['method']} {item['endpoint']}`" if item["endpoint"] else f"[See API reference]({item['api_reference_url']})"
    return f"""# {item['title']}

{item['description']}

## What this example does

{item['operation']}

| Interface | Value |
| --- | --- |
| Agent | {agent_name} |
| MCP tool | `{item['mcp_tool']}` |
| API endpoint | {endpoint_value} |

## Before you run it

1. Connect Medux MCP to {agent_name}.
2. Authenticate with your Medux credential.
3. Prepare any source files or IDs referenced by the request fields below.
4. Review the proposed tool arguments before approving the call.

## Prompt

```text
{item['prompt']}
```

The same prompt is available in [`prompt.txt`](./prompt.txt) for easy copying.

## Request fields

| Field | Type | Requirement | Purpose |
| --- | --- | --- | --- |
{field_rows}

## Run the workflow

1. Paste the prompt into {agent_name}.
2. Confirm that {agent_name} selects `{item['mcp_tool']}`.
3. Replace placeholders with your real file, asset, task, model, or text values.
4. Review and approve the MCP tool call.
5. If the response contains an asynchronous task, monitor it until completion and save the returned result IDs or URLs.

## Resources

- [Complete tutorial]({item['tutorial_url']})
- [API reference]({item['api_reference_url']})
- [All Medux tutorials](https://medux.io/tutorials/)
- [Medux MCP overview](https://medux.io/overview/mcp)

> The API reference is the source of truth for current fields, limits, and response semantics.
"""


def render_root(items: list[dict]) -> str:
    groups: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        groups[item["category"]].append(item)
    sections = []
    for category in sorted(groups):
        rows = [f"### {category.title()}", "", "| Example | Claude | Codex |", "| --- | --- | --- |"]
        by_slug: dict[str, dict[str, dict]] = defaultdict(dict)
        for item in groups[category]:
            by_slug[item["slug"]][item["agent"]] = item
        for slug, variants in sorted(by_slug.items()):
            label = next(iter(variants.values()))["title"]
            label = re.sub(r" with (?:Claude|Codex) MCP and Medux$", "", label)
            claude = f"[Example](./examples/claude/{slug}/)" if "claude" in variants else "—"
            codex = f"[Example](./examples/codex/{slug}/)" if "codex" in variants else "—"
            rows.append(f"| {label} | {claude} | {codex} |")
        sections.append("\n".join(rows))
    sections_text = "\n\n".join(sections)
    return f"""# Medux API Examples

Practical examples for running Medux media and document operations through MCP with Claude and Codex.

## Start here

- [Medux API overview](https://medux.io/overview/api)
- [Connect Medux MCP](https://medux.io/overview/mcp)
- [Browse the complete tutorials](https://medux.io/tutorials/)
- [API reference](https://medux.io/api-reference)

## How to use an example

1. Open an example for your agent.
2. Copy its `prompt.txt` into Claude or Codex.
3. Replace placeholders with your own IDs, files, prompts, and settings.
4. Review the selected Medux MCP tool and its arguments.
5. Approve the call and monitor asynchronous tasks to completion.

## Examples

This repository currently contains **{len(items)} agent examples** generated from the published Medux tutorials.

{sections_text}

## Repository layout

```text
examples/
├── claude/<operation>/
│   ├── README.md
│   ├── prompt.txt
│   └── example.json
└── codex/<operation>/
    ├── README.md
    ├── prompt.txt
    └── example.json
```

## Source and maintenance

The example catalog is generated from the canonical tutorial HTML. Run `python3 scripts/generate_examples.py --source /path/to/tutorials` after tutorial changes, then run `python3 scripts/validate_examples.py`.

## Security

Never commit Medux credentials, API keys, private asset IDs, or private media URLs. Review every agent-proposed tool call before approving it.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=Path("../tutorials"))
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    source = args.source.resolve()
    repo = args.repo.resolve()
    paths = sorted(path for path in source.glob("*.html") if path.name != "index.html")
    items = [parse_tutorial(path) for path in paths]

    examples_root = repo / "examples"
    if examples_root.exists():
        for generated in examples_root.glob("*/*/*"):
            if generated.is_file():
                generated.unlink()
        for directory in sorted(examples_root.glob("*/*"), reverse=True):
            if directory.is_dir() and not any(directory.iterdir()):
                directory.rmdir()

    for item in items:
        target = examples_root / item["agent"] / item["slug"]
        target.mkdir(parents=True, exist_ok=True)
        (target / "README.md").write_text(render_example(item), encoding="utf-8")
        (target / "prompt.txt").write_text(item["prompt"] + "\n", encoding="utf-8")
        (target / "example.json").write_text(json.dumps(item, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    (repo / "examples.json").write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (repo / "README.md").write_text(render_root(items), encoding="utf-8")
    print(f"Generated {len(items)} examples from {source}")


if __name__ == "__main__":
    main()
