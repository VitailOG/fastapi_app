from sqlalchemy import UnicodeText

from src.models.base import Base
from src.models.mixin import IdentityModelMixin
from src.utils.models.column_required import RequiredColumn


class Department(IdentityModelMixin, Base):
    """ Departments in the educational institution.
    """
    name = RequiredColumn(UnicodeText)
