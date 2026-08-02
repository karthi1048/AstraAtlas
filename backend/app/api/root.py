from fastapi import APIRouter
from app.core.config import get_settings

router = APIRouter()
settings = get_settings()

@router.get("/")
def root():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
        "status": "running",
    }