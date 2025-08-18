from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.dependencies import get_identity

router = APIRouter()

@router.get("/whoami", status_code=200)
def whoami(identity: str = Depends(get_identity)):
    return JSONResponse(content={"identity": f"Hi , I am service {identity}"}, status_code=200)
