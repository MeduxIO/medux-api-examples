#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X GET 'https://api.medux.io/api/app/v1/results?cursor=CURSOR&limit=LIMIT&media_type=MEDIA_TYPE&capability_id=CAPABILITY_ID&status=READY' \
  -H "Authorization: Bearer $MEDUX_API_KEY"
