#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X GET 'https://api.medux.io/api/app/v1/clone/avatars?cursor=CURSOR&limit=LIMIT' \
  -H "Authorization: Bearer $MEDUX_API_KEY"
