from pydantic import BaseModel
import uuid

class DeanModel(BaseModel):
    id : uuid.UUID
    name: str
    fullname: str
    specialty: str
    contract_type: str  
    experience: int
    email: str
    username: str
    

class DeanCreateModel(BaseModel):
    name: str
    fullname: str
    email: str
    specialty: str
    contract_type: str
    experience: int
    username: str
    password: str