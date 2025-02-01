from pydantic import BaseModel
import uuid
from backend.domain.schemas.user import UserCreateModel


class DeanModel(BaseModel):
    id : uuid.UUID
    name: str
    lastname: str
    lastname: str
    specialty: str
    contract_type: str  
    experience: int
    email: str
    username: str
    

class DeanCreateModel(UserCreateModel):
    specialty: str
    contract_type: str
    experience: int