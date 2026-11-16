"""Runnable example generated from the official Medux API Reference."""

import json
import os

import requests

BASE_URL = os.getenv("MEDUX_API_BASE_URL", "https://api.medux.io")
PLACEHOLDERS = frozenset(['FILE_ID', 'MODEL_ID'])


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


path = "/api/app/v1/process/video/background_removal"
url = f"{BASE_URL}{path}"

payload = resolve_placeholders(json.loads(r'''
{
  "file_id": "FILE_ID",
  "model_id": "MODEL_ID",
  "region": {
    "height": 1,
    "width": 1,
    "x": 1,
    "y": 1
  },
  "title": "Demo title"
}
'''))

response = requests.request(
    "POST",
    url,
    headers={"Authorization": f"Bearer {require_env('MEDUX_API_KEY')}"},
    json=payload,
    timeout=120,
)
response.raise_for_status()
result = response.json()
if result.get("code") not in (None, 0):
    raise RuntimeError(f"Medux API error: {result.get('code')} {result.get('message')}")
print(json.dumps(result, indent=2))
