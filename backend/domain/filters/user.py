from pydantic import BaseModel, Field
from typing import Optional

class ChangeRequest(BaseModel) :
    username : Optional[str] = None
    hash_password : Optional[str] = Field(None, alias="password")