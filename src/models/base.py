from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls):
        return name if (name := cls.__name__.lower()).endswith('s') else name + 's'
