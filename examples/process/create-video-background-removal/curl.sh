#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/process/video/background_removal \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"file_id":"FILE_ID","model_id":"MODEL_ID","region":{"height":1,"width":1,"x":1,"y":1},"title":"Demo title"}'
