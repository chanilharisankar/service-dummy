from fastapi import FastAPI
from app.routers import health, whoami

app = FastAPI()

app.include_router(health.router)
app.include_router(whoami.router)
