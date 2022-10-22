from fastapi import APIRouter

from . import student

router = APIRouter()

router.include_router(student.router, tags=["student"], prefix="/student")
