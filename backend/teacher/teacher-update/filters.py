from pydantic import BaseModel
from typing import Optional

class ChangeRequest(BaseModel) :
    name : Optional[str] = None
    full_name : Optional[str] = None
    email : Optional[str] = None
    specialty : Optional[str] = None
    contract_type : Optional[str] = None
    experience : Optional[int] = None
    username : Optional[str] = None
    hash_password : Optional[str] = None
