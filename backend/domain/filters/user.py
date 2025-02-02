from pydantic import BaseModel, Field
from typing import Optional

class UserChangeRequest(BaseModel) :
    username : Optional[str] = None
    email : Optional[str] = None

class UserPasswordChangeRequest(BaseModel) :
    current_password : str | None = None
    new_password : str | None = None