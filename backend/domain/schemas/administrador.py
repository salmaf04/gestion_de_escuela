from pydantic import BaseModel
import uuid

class AdministratorCreateModel(BaseModel):
    name: str
    username: str
    email: str
    password: str


class AdministratorModel(BaseModel):
    id : uuid.UUID
    name: str
    username: str
    email: str
    hash_password: str

