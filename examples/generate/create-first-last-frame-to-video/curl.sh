#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/generate/video/first_last_frame_to_video \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"aspect_ratio":"ASPECT_RATIO","clarity":"CLARITY","duration_seconds":1,"image_file_ids":["FILE_ID"],"model_id":"MODEL_ID","prompt":"PROMPT","title":"Demo title"}'
