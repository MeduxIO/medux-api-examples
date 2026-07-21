#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/generate/video/image_audio_driven \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model_id":"image-audio-driven-video-default","prompt_audio_file_id":"AUDIO_FILE_ID","prompt_image_file_id":"FILE_ID","prompt_text":"Hello from Medux","resolution":"720p"}'
