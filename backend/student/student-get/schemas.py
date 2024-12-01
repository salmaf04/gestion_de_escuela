from pydantic import BaseModel, Field
import uuid

class StudentModel(BaseModel):
    id : uuid.UUID
    name: str
    age: int
    email: str = Field(alias="email")
    extra_activities: bool