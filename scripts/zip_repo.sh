#!/usr/bin/env bash
set -euo pipefail
cd ..
zip -r agent-overseer.zip agent-overseer \
  -x "*/__pycache__/*" "*/.venv/*" "*/node_modules/*" "*/.DS_Store"
echo "Created agent-overseer.zip"
