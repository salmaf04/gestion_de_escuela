from pydantic import BaseModel
import uuid

class SecretaryModel(BaseModel):
    id : uuid.UUID
    name: str