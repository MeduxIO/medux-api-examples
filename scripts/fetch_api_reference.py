#!/usr/bin/env python3
"""Download the structured Medux API Reference embedded in the public site."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import subprocess
import time
from pathlib import Path


BASE_URL = "https://medux.io"
INDEX_URL = f"{BASE_URL}/api-reference/"
FLIGHT_CHUNK_RE = re.compile(
    r'self\.__next_f\.push\(\[1,("(?:\\.|[^"\\])*")\]\)</script>',
    re.S,
)


def download(url: str) -> str:
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            result = subprocess.run(
                [
                    "curl",
                    "--http1.1",
                    "-L",
                    "--retry",
                    "1",
                    "--retry-all-errors",
                    "--fail",
                    "--silent",
                    "--show-error",
                    "--max-time",
                    "12",
                    url,
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            return result.stdout
        except Exception as error:  # pragma: no cover - network retry
            last_error = error
            if attempt < 2:
                time.sleep(1 + attempt)
    raise RuntimeError(f"Unable to download {url}: {last_error}")


def flight_data(page_html: str) -> str:
    chunks = [json.loads(match.group(1)) for match in FLIGHT_CHUNK_RE.finditer(page_html)]
    if not chunks:
        raise ValueError("Next.js flight data was not found")
    return "".join(chunks)


def decode_property(data: str, property_name: str):
    marker = f'"{property_name}":'
    position = data.find(marker)
    if position < 0:
        raise ValueError(f"Missing {property_name} in Next.js flight data")
    value, _ = json.JSONDecoder().raw_decode(data, position + len(marker))
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "api-reference.json",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / ".cache" / "api-reference",
    )
    args = parser.parse_args()
    args.cache_dir.mkdir(parents=True, exist_ok=True)

    index_data = flight_data(download(INDEX_URL))
    groups = decode_property(index_data, "initialSiteGroups")
    routes = [
        (group["slug"], item["endpoint_slug"])
        for group in groups
        for item in group["items"]
        if item.get("page_type") == "API_REFERENCE"
    ]

    def fetch_route(route: tuple[str, str]) -> dict:
        module, slug = route
        source_url = f"{BASE_URL}/api-reference/{module}/{slug}"
        cache_file = args.cache_dir / f"{module}--{slug}.html"
        if cache_file.exists():
            page_html = cache_file.read_text(encoding="utf-8")
        else:
            page_html = download(source_url)
            cache_file.write_text(page_html, encoding="utf-8")
        page = decode_property(flight_data(page_html), "initialPage")
        if page["meta"]["module"] != module or page["meta"]["endpoint_slug"] != slug:
            raise ValueError(f"Reference route mismatch at {source_url}")
        page["source_url"] = source_url
        return page

    with concurrent.futures.ThreadPoolExecutor(max_workers=24) as executor:
        endpoints = list(executor.map(fetch_route, routes))

    for index, page in enumerate(endpoints, start=1):
        module = page["meta"]["module"]
        slug = page["meta"]["endpoint_slug"]
        print(f"[{index:02d}/{len(routes):02d}] {module}/{slug}")

    output = {
        "source": INDEX_URL,
        "endpoint_count": len(endpoints),
        "groups": groups,
        "endpoints": endpoints,
    }
    args.output.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(endpoints)} endpoints to {args.output}")


if __name__ == "__main__":
    main()
