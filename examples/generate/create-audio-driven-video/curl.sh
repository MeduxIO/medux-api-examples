#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/generate/video/audio_driven \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"aspect_ratio":"ASPECT_RATIO","audio_file_id":"AUDIO_FILE_ID","avatar_asset_id":"AVATAR_ASSET_ID","clarity":"CLARITY","duration_seconds":1,"links":["https://example.com/reference"],"model":"MODEL","model_id":"MODEL_ID","title":"Demo title"}'
