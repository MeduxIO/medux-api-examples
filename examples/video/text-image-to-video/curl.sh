#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/generate/video/text_image_to_video \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"height":832,"model_id":"text-image-to-video-default","num_frames":124,"prompt_text":"Hello from Medux","resolution":"480p","seed":-1,"width":480}'
