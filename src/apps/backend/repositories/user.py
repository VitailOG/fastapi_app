from sqlalchemy import select

from src.models.user import User
from src.models.main import Department
from .base import BaseRepository
from ..api.schemas.user import BaseUserSchema


class UserRepository(BaseRepository[User]):
    model: User = User

    async def get_user_by_id(self):
        q = select(User)
        res = await self.dbsession.execute(q)
        return res.scalars().all()

    async def create_user(self, data: BaseUserSchema):
        new_user = User(**data.dict())
        self.dbsession.add(new_user)
        await self.dbsession.commit()
