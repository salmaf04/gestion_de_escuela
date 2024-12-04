from pydantic import BaseModel
from typing import Optional

class ChangeRequest(BaseModel) :
    state : Optional[str] = None
    location : Optional[str] = None