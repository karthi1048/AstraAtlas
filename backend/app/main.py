import logging
from fastapi import FastAPI
from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.core.exceptions import register_exception_handlers

configure_logging()
settings = get_settings()

# automatically names the logger after the current module
logger = logging.getLogger(__name__)

# THis reads metadata from configuration (Settings Object)
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

logger.info("AstraAtlas backend started successfully.")

register_exception_handlers(app)

app.include_router(api_router)