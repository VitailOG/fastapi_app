from beanie import Document


class Message(Document):
    name: str
    user_id: int

    class Settings:
        name = "message_user"
