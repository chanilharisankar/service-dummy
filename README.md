# service-dummy

A dummy Python FastAPI microservice with Docker support and Makefile automation.

## Features
- FastAPI app with two endpoints:
  - `/health`: Returns HTTP 200 and `{ "status": "ok" }`
  - `/whoami`: Returns HTTP 200 and `{ "identity": "Hi , I am service <name>" }`, where `<name>` is set via environment variable `SERVICE_NAME` (defaults to `foo`)
- Production-grade folder structure
- Dockerfile for containerization
- Makefile for start/stop automation
- Unit tests with pytest

## Getting Started

### Prerequisites
- Python 3.11+
- Docker
- Make

### Local Development
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Start service:
   ```sh
   make start SERVICE_NAME=foo
   ```
3. Stop service:
   ```sh
   make stop
   ```

### Run with Docker
1. Build image:
   ```sh
   docker build -t service-dummy .
   ```
2. Run container:
   ```sh
   docker run -p 8000:8000 -e SERVICE_NAME=foo service-dummy
   ```

### API Endpoints
- `GET /health` → `{ "status": "ok" }`
- `GET /whoami` → `{ "identity": "Hi , I am service <name>" }`

### Run Tests
```sh
pytest
```
