from pydantic import BaseModel
import uuid
from backend.domain.schemas.user import UserCreateModel

class SecretaryModel(BaseModel):
    id : uuid.UUID
    name: str
    lastname: str
    username: str
    email: str
    hash_password: str
    
class SecretaryCreateModel(UserCreateModel):
    pass