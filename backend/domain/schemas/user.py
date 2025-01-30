import uuid
from pydantic import BaseModel, Field, field_validator
from backend.domain.schemas.exceptions import ValidationException
from fastapi import HTTPException


class UserCreateModel(BaseModel):
    username: str
    email: str

    @classmethod
    def parse_email(cls, email):
        parsed_email = email.split("@")
        parsed_email_result  = parsed_email[1].split(".")
        return parsed_email_result


    @field_validator("email")
    def email_must_be_valid(cls, email):
        parsed_email = cls.parse_email(email)
        
        try :
            if len(parsed_email) != 2:
                raise ValidationException("Invalid email")
            
            if parsed_email[0] != "gmail":
                raise ValidationException(message="Invalid email")
            
            if parsed_email[1] != "com":
                raise ValidationException("Invalid email")
        except ValidationException as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        return email


class UserModel(BaseModel) :
    id: uuid.UUID
    username: str
    email: str
    hashed_password: str 
    type: str

class UserLoginModel(BaseModel) :
    email: str
    password: str
