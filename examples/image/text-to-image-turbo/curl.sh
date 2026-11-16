#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/generate/image/text_to_image_turbo \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"height":1024,"model_id":"zimage-turbo","prompt":"An isometric 3D render of a media pipeline: video, image and audio tiles flowing through a single glowing violet hub on a dark studio background, soft volumetric light, crisp product-shot detail","width":1024}'
