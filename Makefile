SERVICE_NAME ?= foo
PID_FILE := service.pid

start:
	@echo "Starting service with identity $(SERVICE_NAME)"
	@bash start.sh $(SERVICE_NAME) & echo $$! > $(PID_FILE)

stop:
	@if [ -f $(PID_FILE) ]; then \
		PID=$$(cat $(PID_FILE)); \
		echo "Stopping service with PID $$PID"; \
		kill $$PID; \
		rm -f $(PID_FILE); \
	else \
		echo "Service not running."; \
	fi

.PHONY: start stop
