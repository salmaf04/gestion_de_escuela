from pydantic import BaseModel

class UserCreateModel(BaseModel) :
    username: str
    email: str
    password: str