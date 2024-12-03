import uuid
from pydantic import BaseModel, Field


class UserCreateModel(BaseModel) :
    username: str
    email: str
    password: str = Field(exclude=True)


class UserModel(BaseModel) :
    id: uuid.UUID
    username: str
    email: str
    hashed_password: str = Field(exclude=True)
    type: str

class UserLoginModel(BaseModel) :
    email: str
    password: str
