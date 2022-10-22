from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.models import engine
from src.models.base import Base
from src.models.message import Message
from src.config import settings


async def init_mongo():
    client = AsyncIOMotorClient(settings.MONGO_URI)
    await init_beanie(database=client.db_name, document_models=[Message])
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

