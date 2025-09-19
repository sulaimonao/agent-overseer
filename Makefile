.ONESHELL:
SHELL := /bin/bash

PY := .venv/bin/python
PIP := .venv/bin/pip

.PHONY: venv install dev zip

venv:
	python3 -m venv .venv

install: venv
	source .venv/bin/activate
	$(PIP) install -r agent_core/requirements.lock.txt

dev:
	source .venv/bin/activate
	cd agent_core && uvicorn app:app --reload --host 127.0.0.1 --port 8000

zip:
	bash scripts/zip_repo.sh
