from typing import Literal
from pydantic import BaseModel


class BaseUserSchema(BaseModel):
    username: str
    last_name: str
    middle_name: str
    password: str
    first_name: str
    gender: Literal['male', 'female']


class UserResponseSchema(BaseUserSchema):
    id: int

    class Config:
        orm_mode = True
