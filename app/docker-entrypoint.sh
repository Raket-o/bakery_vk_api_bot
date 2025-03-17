#!/usr/bin/env bash

uv run alembic downgrade head
uv run uvicorn app.main:app --host 192.168.55.5 --port 8000
