from fastapi import APIRouter, Depends

from src.apps.backend.repositories.user import UserRepository
from src.apps.backend.api.dependencies.db import get_repository
from src.apps.backend.api.schemas.user import UserResponseSchema, BaseUserSchema
from src.lib.celery.tasks import t
from src.models.message import Message

router = APIRouter()


@router.post('/', response_model=list[UserResponseSchema])
async def ping(
        user: UserRepository = Depends(get_repository(UserRepository))
):
    return await user.get_user_by_id()


@router.post('/create-user')
async def create_user(
        data: BaseUserSchema,
        user: UserRepository = Depends(get_repository(UserRepository))
):
    await user.create_user(data)


@router.post('/cr')
async def cuser():
    await Message(name="Tony's", user_id=1).insert()


@router.get('/qwe')
async def c():
    foo = await Message.find(Message.name == "Tony's").to_list()
    return foo


@router.post('/task', tags=['celery'])
async def celery_task():
    t.delay()
    return {"celery": "task"}
