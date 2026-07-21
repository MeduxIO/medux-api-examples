#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X GET 'https://api.medux.io/api/app/v1/tasks?cursor=CURSOR&limit=LIMIT&status=QUEUED&media_type=MEDIA_TYPE&capability_id=CAPABILITY_ID' \
  -H "Authorization: Bearer $MEDUX_API_KEY"
