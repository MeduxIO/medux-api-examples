#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/tasks/TASK_ID/sync \
  -H "Authorization: Bearer $MEDUX_API_KEY"
