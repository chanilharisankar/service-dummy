import os

def get_identity():
    # Prefer environment variable SERVICE_NAME, fallback to 'foo'
    return os.environ.get("SERVICE_NAME", "foo")
