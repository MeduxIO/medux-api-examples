#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/process/video/character_replacement_plus \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model_id":"character-replacement-plus-default","source_video_file_id":"FILE_ID","target_character_image_file_id":"FILE_ID"}'
