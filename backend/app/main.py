from fastapi import FastAPI
from app.core.config import get_settings

settings = get_settings()

# THis reads metadata from configuration (Settings Object)
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

@app.get("/")
def root():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
        "status": "running",
    }

@app.get("/health")
def health():
    return {
        "status": "running",
    }