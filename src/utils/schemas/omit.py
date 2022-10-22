from typing import Optional

from pydantic.main import ModelMetaclass


class Omit(ModelMetaclass):
    """
        Example
            class Test(BaseModel, metaclass=Omit):
                name: str
                age: int

                class Config:
                    omit_fields = ['age']
    """
    def __new__(cls, name, bases, namespaces, **kwargs):
        fields = []
        annotations = namespaces.get('__annotations__', {})
        config = namespaces.get('Config', False)

        if config and (omit_fields := getattr(config, 'omit_fields', False)):
            fields = omit_fields

        for base in bases:
            if base_field := getattr(base.Config, 'omit_fields', False):
                fields.extend(base_field)

            annotations.update(base.__annotations__)

        for field in annotations:
            if field not in fields:
                annotations[field] = Optional[annotations[field]]
        return super().__new__(cls, name, bases, namespaces, **kwargs)
