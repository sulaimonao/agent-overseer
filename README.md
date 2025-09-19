# Agent Overseer (Starter)

Local OS overseer agent (macOS-first, cross-OS ready) with safe tool calls and a stable, pinned environment.

## Quickstart

### Option A: one-command bootstrap

```bash
./scripts/bootstrap_env.sh
```

This creates a `.venv`, installs locked Python dependencies, and copies `agent_core/.env.example` to `agent_core/.env` if you have not configured it yet.

### Option B: manual setup

1. **Create a Python virtual environment** and activate it:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies**:

   ```bash
   pip install -r agent_core/requirements.lock.txt
   ```

3. **Set up your environment variables**. Copy the example env file and set the `MODEL_ID` to the tag of the local model you have available in Ollama. Example:

   ```bash
   cp agent_core/.env.example agent_core/.env
   # then edit agent_core/.env to choose your MODEL_ID, e.g. gpt-oss:20b-q4_0
   ```

4. **Run the development server** using the supplied `Makefile`:

   ```bash
   make dev
   ```

   This starts a FastAPI server on `http://127.0.0.1:8000` with hot-reload.

## Features

- **Read-first, confirm-later policy** – The agent collects system information and proposes a plan before making changes. Write operations require explicit confirmation.
- **System mapping** – Gather OS, CPU, memory, disk, network, and process information into a local SQLite database via the `sys_info` tool.
- **Modular tools** – Utilities for reading files (`fs_read`), mapping system state (`sys_info`), searching logs (`logs_query`), and planning/executing changes (`plan_exec`).
- **Extensible architecture** – Add new tools or extend existing ones by implementing functions in `agent_core/agent/tools` and registering them in `TOOLS`.
- **Cross-platform ready** – Designed for macOS initially; abstractions and prompts make it straightforward to add Linux and Windows support.

## Development

- The code lives in the `agent_core` package. The entrypoint for the FastAPI application is `agent_core/app.py`.
- Use `make dev` to run the API locally with auto-reload.
- Use `make zip` to generate a zip archive of the repository (excluding virtual environments and node modules).

## Safety considerations

The starter implementation does **not** execute any system modifications. The `plan_exec.execute` function logs the confirmation but returns a dry-run response. Before enabling write operations you should implement proper permission checks and command execution logic, and always keep the user in control.

## License

This repository is provided as a reference implementation and is open for you to build upon. See the LICENSE file (to be added) for terms of use.
