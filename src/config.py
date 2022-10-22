import os

from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # CELERY_BACKEND_URL: str = "redis://localhost/0"
    # CELERY_BROKER_URL: str = "redis://localhost/0"
    CELERY_BACKEND_URL: str = Field(..., env='CELERY_BACKEND_URL')
    CELERY_BROKER_URL: str = Field(..., env='CELERY_BROKER_URL')
    API_TOKEN: str = '5677558917:AAFLDX-FHia83vuONJAYMEggrz1mJT5aIZU'
    DATABASE_URI: str = Field(..., env='DB_URL')
    MONGO_URI: str = Field(..., env='MONGO_URL')

    class Config:
        env_file = os.getenv('ENV_FILE')
        env_file_encoding = "utf-8"


@lru_cache()
def cached_settings():
    return Settings()


settings = cached_settings()
