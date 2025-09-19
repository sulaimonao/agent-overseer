#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
REPO_NAME="$(basename "${REPO_ROOT}")"

cd "${REPO_ROOT}/.."
zip -r "${REPO_NAME}.zip" "${REPO_NAME}" \
  -x "*/__pycache__/*" "*/.venv/*" "*/node_modules/*" "*/.DS_Store"
echo "Created ${REPO_NAME}.zip"
