import logging
from fastapi import APIRouter
from app.core.config import get_settings

router = APIRouter()
settings = get_settings()

logger = logging.getLogger(__name__)

@router.get("/")
def root():
    logger.info("Root endpoint accessed.")

    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
        "status": "running",
    }

# Temporary test route
# @router.get("/error")
# def trigger_error():
#     raise RuntimeError("Testing global exception handler.")