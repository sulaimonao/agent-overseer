#!/usr/bin/env bash
set -euo pipefail

# Bootstrap a local development environment for Agent Overseer.
#
# This script creates a Python virtual environment, installs the required
# dependencies, and copies the example environment file so you can
# configure the Ollama host and model ID. It is safe to run multiple times.

python3 -m venv .venv
source .venv/bin/activate
pip install -r agent_core/requirements.lock.txt
if [ ! -f agent_core/.env ]; then
  cp agent_core/.env.example agent_core/.env
fi
echo "Environment prepared. Edit agent_core/.env as needed and run 'make dev' to start the server."
