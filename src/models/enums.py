from sqlalchemy.dialects.postgresql import ENUM


Gender = ENUM("male", "female", name="gender")

UserType = ENUM("student", "methodist", "administration", "admin", name="user_type")
