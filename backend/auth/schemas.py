import uuid
from pydantic import BaseModel, Field


class UserCreateModel(BaseModel) :
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


class UserModel(BaseModel) :
    id: uuid.UUID
    username: str
    email: str
    hashed_password: str = Field(exclude=True)
    first_name: str
    last_name: str


class UserLoginModel(BaseModel) :
    email: str
    password: str
