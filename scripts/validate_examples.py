#!/usr/bin/env python3
"""Validate generated Medux API examples."""

from __future__ import annotations

import ast
import json
import re
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
REQUIRED_FILES = {"README.md", "curl.sh", "example.py", "example.mjs", "request.json", "reference.json"}
SECRET_PATTERNS = [
    re.compile(r"(?:api[_-]?key|authorization)\s*[:=]\s*['\"]?(?!your|<|\{|f\"|`)[A-Za-z0-9_-]{20,}", re.I),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def main() -> None:
    failures: list[str] = []
    snapshot = json.loads((REPO / "api-reference.json").read_text(encoding="utf-8"))
    index = json.loads((REPO / "examples.json").read_text(encoding="utf-8"))
    unavailable = json.loads((REPO / "unavailable-sample-previews.json").read_text(encoding="utf-8"))
    endpoints = snapshot["endpoints"]
    documented_previews = {
        sample["sample_output"]["preview_url"]
        for page in endpoints
        for sample in page.get("examples", {}).get("samples", [])
        if sample.get("sample_output", {}).get("preview_url")
    }
    unknown_unavailable = set(unavailable.get("urls", [])) - documented_previews
    if unknown_unavailable:
        failures.append("unavailable preview list contains URLs absent from API Reference")

    if snapshot["endpoint_count"] != len(endpoints):
        failures.append("api-reference.json endpoint_count does not match endpoints")
    if len(index) != len(endpoints):
        failures.append("examples.json does not match API Reference endpoint count")
    if (REPO / "examples" / "claude").exists() or (REPO / "examples" / "codex").exists():
        failures.append("API examples must not be partitioned by Claude or Codex")

    expected_dirs = set()
    for page in endpoints:
        meta = page["meta"]
        target = REPO / "examples" / meta["module"] / meta["endpoint_slug"]
        expected_dirs.add(target)
        missing = REQUIRED_FILES - {path.name for path in target.glob("*") if path.is_file()}
        if missing:
            failures.append(f"{target.relative_to(REPO)} missing: {', '.join(sorted(missing))}")
            continue
        readme = (target / "README.md").read_text(encoding="utf-8")
        for heading in ("## Endpoint", "## Authentication", "## Request", "## curl", "## Python", "## JavaScript", "## Response", "## MCP alternative", "## Source of truth"):
            if heading not in readme:
                failures.append(f"{target.relative_to(REPO)}/README.md missing {heading}")
        reference = json.loads((target / "reference.json").read_text(encoding="utf-8"))
        if reference["source_url"] != page["source_url"]:
            failures.append(f"{target.relative_to(REPO)} reference mismatch")
        try:
            ast.parse((target / "example.py").read_text(encoding="utf-8"))
        except SyntaxError as error:
            failures.append(f"{target.relative_to(REPO)}/example.py: {error}")
        shell = subprocess.run(["bash", "-n", str(target / "curl.sh")], capture_output=True, text=True)
        if shell.returncode:
            failures.append(f"{target.relative_to(REPO)}/curl.sh: {shell.stderr.strip()}")
        node = subprocess.run(["node", "--check", str(target / "example.mjs")], capture_output=True, text=True)
        if node.returncode:
            failures.append(f"{target.relative_to(REPO)}/example.mjs: {node.stderr.strip()}")

    actual_dirs = {path for path in (REPO / "examples").glob("*/*") if path.is_dir()}
    for extra in actual_dirs - expected_dirs:
        failures.append(f"unexpected example directory: {extra.relative_to(REPO)}")

    markdown_link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for markdown in REPO.rglob("*.md"):
        if ".git" in markdown.parts or ".cache" in markdown.parts:
            continue
        for target in markdown_link.findall(markdown.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            local_target = target.split("#", 1)[0].split("?", 1)[0]
            if local_target and not (markdown.parent / local_target).resolve().exists():
                failures.append(f"broken local link in {markdown.relative_to(REPO)}: {target}")

    for path in REPO.rglob("*"):
        if not path.is_file() or ".git" in path.parts or ".cache" in path.parts:
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
    print(f"Validated {len(endpoints)} API examples")


if __name__ == "__main__":
    main()
