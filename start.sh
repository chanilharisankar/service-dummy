#!/bin/bash
# Entrypoint script for starting FastAPI service with identity argument
SERVICE_NAME="${SERVICE_NAME:-${1:-foo}}"
export SERVICE_NAME
echo "{\"event\": \"service_start\", \"service_name\": \"$SERVICE_NAME\"}"
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
