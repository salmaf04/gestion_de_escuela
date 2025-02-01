from pydantic import BaseModel
from typing import Optional

class AdministratorChangeRequest(BaseModel) :
    name : Optional[str] = None
    username : Optional[str] = None
    email : Optional[str] = None
    hash_password : Optional[str] = None
