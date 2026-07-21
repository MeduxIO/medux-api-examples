#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/assets \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"category":"MEDIA","file_size_bytes":1,"name":"NAME","storage_object":{"key":"STORAGE_OBJECT_KEY","url":"https://example.com/callback"}}'
