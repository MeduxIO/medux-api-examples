#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/process/image/outfit_swap \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model_id":"image-outfit-swap-default","source_image_file_id":"FILE_ID","target_outfit_image_file_id":"FILE_ID"}'
