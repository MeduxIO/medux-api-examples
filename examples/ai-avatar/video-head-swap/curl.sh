#!/usr/bin/env bash
set -euo pipefail
: "${MEDUX_API_KEY:?Set MEDUX_API_KEY}"

curl -X POST https://api.medux.io/api/app/v1/process/video/animate_head_swap \
  -H "Authorization: Bearer $MEDUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"edit_prompt":"人脸保持不变","face_image_file_id":"FILE_ID","height":832,"input_video_file_id":"FILE_ID","model_id":"animate-head-swap-default","positive_prompt":"一个角色在说话","width":480}'
