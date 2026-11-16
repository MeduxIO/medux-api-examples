#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/process/video/face_swap_plus \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"input_video_file_id":"FILE_ID","model_id":"face-swap-plus-default","source_image_file_id":"FILE_ID"}'
