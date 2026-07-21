#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/process/asset/pdf_to_excel \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"flavor":"stream","input_file_id":"FILE_ID","model_id":"pdf-to-excel-default","pages":"all"}'
