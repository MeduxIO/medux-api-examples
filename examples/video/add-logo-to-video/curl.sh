#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/process/video/add_logo_to_video \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"logo_file_id":"FILE_ID","model_id":"add-logo-to-video-default","video_file_id":"FILE_ID","x":10,"y":10}'
