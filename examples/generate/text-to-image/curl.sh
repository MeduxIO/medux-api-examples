#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/generate/image/text_to_image \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"cfg_normalization":false,"cfg_truncation":1,"guidance_scale":0,"height":1024,"max_sequence_length":512,"model_id":"text-to-image-default","num_inference_steps":9,"prompt":"PROMPT","seed":-1,"width":1024}'
