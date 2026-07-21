#!/usr/bin/env python3
"""Validate the generated Medux example catalog without network access."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = [
    re.compile(r"(?:api[_-]?key|authorization)\s*[:=]\s*['\"]?(?!your|<|\{)[A-Za-z0-9_-]{20,}", re.I),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def main() -> None:
    failures: list[str] = []
    manifest_path = REPO / "examples.json"
    if not manifest_path.exists():
        failures.append("examples.json is missing")
        items = []
    else:
        items = json.loads(manifest_path.read_text(encoding="utf-8"))

    ids = [item.get("id") for item in items]
    if len(ids) != len(set(ids)):
        failures.append("examples.json contains duplicate ids")

    for item in items:
        target = REPO / "examples" / item["agent"] / item["slug"]
        for name in ("README.md", "prompt.txt", "example.json"):
            if not (target / name).is_file():
                failures.append(f"missing {target / name}")
        for key in ("title", "description", "mcp_tool", "prompt", "tutorial_url", "api_reference_url"):
            if not item.get(key):
                failures.append(f"{item.get('id')}: missing {key}")
        if not str(item.get("tutorial_url", "")).startswith("https://medux.io/tutorials/"):
            failures.append(f"{item.get('id')}: invalid tutorial URL")
        if not str(item.get("api_reference_url", "")).startswith("https://medux.io/api-reference/"):
            failures.append(f"{item.get('id')}: invalid API reference URL")

    for path in REPO.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                failures.append(f"possible secret in {path.relative_to(REPO)}")

    if failures:
        print("Validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Validated {len(items)} examples")


if __name__ == "__main__":
    main()
