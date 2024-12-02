from pydantic import BaseModel
from typing import Optional

class ChangeRequest(BaseModel) :
    name : Optional[str] = None
    age : Optional[int] = None
    email : Optional[str] = None
    extra_activities : Optional[bool] = None