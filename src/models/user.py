from sqlalchemy import UnicodeText, ForeignKeyConstraint, Integer
from sqlalchemy.orm import declared_attr

from src.utils.models.column_required import RequiredColumn
from .base import Base
from .enums import Gender, UserType
from .main import Department
from .mixin import IdentityModelMixin


class User(IdentityModelMixin, Base):

    username = RequiredColumn(UnicodeText)
    password = RequiredColumn("password", UnicodeText)

    last_name = RequiredColumn(UnicodeText)
    first_name = RequiredColumn(UnicodeText)
    middle_name = RequiredColumn(UnicodeText)

    user_type = RequiredColumn(UserType, server_default='student')
    gender = RequiredColumn(Gender)

    department_id = RequiredColumn(Integer)

    @declared_attr
    def __table_args__(cls):
        return super().__table_args__ + (
            ForeignKeyConstraint(
                ("department_id",),
                (Department.id,)
            ),
        )


class Student: pass
