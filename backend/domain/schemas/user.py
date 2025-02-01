import uuid
from pydantic import BaseModel, Field, field_validator
from backend.domain.schemas.exceptions import ValidationException
from fastapi import HTTPException, status


class UserCreateModel(BaseModel):
    name: str
    lastname: str
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
    
    @field_validator("name")
    def valid_name(cls, name: str) :
        for letter in name :
            if not letter.isalpha() and not letter.isspace():
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail="Su nombre no es valido , contiene caracteres que no son letras"
                )
        return name
    
    @field_validator("lastname")
    def valid_lastname(cls, lastname: str) :
        for letter in lastname :
            if not letter.isalpha() and not letter.isspace():
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail="Su apellido no es valido , contiene caracteres que no son letras"
                )
        return lastname
        

class UserModel(BaseModel) :
    id: uuid.UUID
    username: str
    email: str
    hashed_password: str 
    type: str

class UserLoginModel(BaseModel) :
    email: str
    password: str
