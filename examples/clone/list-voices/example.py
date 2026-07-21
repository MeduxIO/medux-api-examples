"""Runnable example generated from the official Medux API Reference."""

import json
import os

import requests

BASE_URL = os.getenv("MEDUX_API_BASE_URL", "https://api.medux.io")
PLACEHOLDERS = frozenset([])


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Set {name} before running this example")
    return value


def resolve_placeholders(value):
    if isinstance(value, dict):
        return {key: resolve_placeholders(item) for key, item in value.items()}
    if isinstance(value, list):
        return [resolve_placeholders(item) for item in value]
    if isinstance(value, str) and value in PLACEHOLDERS:
        return require_env(value)
    return value


path = "/api/app/v1/clone/voices"
url = f"{BASE_URL}{path}"

params = {}
if os.getenv("CURSOR"):
    params["cursor"] = os.environ["CURSOR"]
if os.getenv("LIMIT"):
    params["limit"] = os.environ["LIMIT"]

response = requests.request(
    "GET",
    url,
    headers={"Authorization": f"Bearer {require_env('MEDUX_API_KEY')}"},
    params=params,
    timeout=120,
)
response.raise_for_status()
result = response.json()
if result.get("code") not in (None, 0):
    raise RuntimeError(f"Medux API error: {result.get('code')} {result.get('message')}")
print(json.dumps(result, indent=2))
