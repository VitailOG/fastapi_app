from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T')


class BaseRepository(Generic[T]):
    model: T = None

    def __init__(self, dbsession: AsyncSession) -> None:
        self._dbsession = dbsession

    @property
    def get_model(self) -> T:
        assert self.model is None
        return self.model

    @property
    def dbsession(self) -> AsyncSession:
        return self._dbsession
