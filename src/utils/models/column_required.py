from sqlalchemy import Column


class RequiredColumn(Column):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nullable = False
