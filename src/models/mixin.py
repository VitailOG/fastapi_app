from sqlalchemy import Column, Integer, Identity, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class IdentityModelMixin:

    id = Column(Integer, Identity(always=True))

    __table_args__ = (
        PrimaryKeyConstraint("id"),
    )
