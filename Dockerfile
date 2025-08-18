
# Use official Python slim image for security and size
FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app
COPY start.sh ./start.sh

# Expose FastAPI default port
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["bash", "start.sh"]
CMD ["foo"]
