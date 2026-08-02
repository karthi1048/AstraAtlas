from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AstraAtlas"
    app_version: str = "0.1.0-alpha.1"
    app_env: str = "development"
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )

# This creates Settings object only once & reuse it
@lru_cache
def get_settings() -> Settings:
    return Settings()