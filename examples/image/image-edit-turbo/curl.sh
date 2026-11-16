#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/generate/image/image_edit_turbo \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"height":1024,"image_file_ids":["FILE_ID"],"model_id":"qwen-image-edit","prompt":"PROMPT","width":1024}'
