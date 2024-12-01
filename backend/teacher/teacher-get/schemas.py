from pydantic import BaseModel, Field
import uuid

class TeacherModel(BaseModel):
    id : uuid.UUID
    name: str
    fullname: str
    email: str = Field(alias="email")
    specialty: str
    contract_type: str
    experience: int