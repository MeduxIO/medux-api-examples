#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/generate/video/mv_director \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"model_id":"mv-director-default","persona":"A rugged middle-aged rock singer with twin hair buns and a jade gourd ornament, wearing aviator sunglasses and a crimson vest with green leaf-shaped lapels, performing at a vintage microphone on a smoky, amber-lit stage, shot on 35mm, warm, gritty, and cinematic.","prompt_audio_file_id":"AUDIO_FILE_ID","prompt_image_file_id":"FILE_ID"}'
