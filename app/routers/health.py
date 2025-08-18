from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health", status_code=200)
def health_check():
    return JSONResponse(content={"status": "ok"}, status_code=200)
