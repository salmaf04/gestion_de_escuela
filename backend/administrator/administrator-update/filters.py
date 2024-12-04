from pydantic import BaseModel
from typing import Optional

class ChangeRequest(BaseModel) :
    name : Optional[str] = None
    username : Optional[str] = None
    email : Optional[str] = None
    hash_password : Optional[str] = None
