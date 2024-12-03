from pydantic import BaseModel
import uuid

class SecretaryCreateModel(BaseModel):
    name: str
    username: str
    email: str
    hash_password: str


class SecretaryModel(BaseModel):
    id : uuid.UUID
    name: str
    username: str
    email: str
    hash_password: str

