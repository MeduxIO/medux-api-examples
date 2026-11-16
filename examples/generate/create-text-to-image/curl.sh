#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/generate/image/text_to_image \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"aspect_ratio":"ASPECT_RATIO","clarity":"CLARITY","image_file_ids":["FILE_ID"],"model_id":"MODEL_ID","prompt":"PROMPT","quantity":1,"title":"Demo title"}'
