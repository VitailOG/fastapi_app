from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.config import settings


SQLALCHEMY_ASYNC_ENGINE_OPTIONS = {
    "echo": True,
    "connect_args": {
        "timeout": 5  # seconds
    },
    "future": True
}

engine = create_async_engine(
    settings.DATABASE_URI,
    **SQLALCHEMY_ASYNC_ENGINE_OPTIONS
)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
