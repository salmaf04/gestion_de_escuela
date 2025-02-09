"""
Pydantic models for user data validation and serialization.
These models define the structure and validation rules for user-related operations.
"""

import uuid
from pydantic import BaseModel, Field, field_validator
from backend.domain.schemas.exceptions import ValidationException
from fastapi import HTTPException, status


class UserCreateModel(BaseModel):
    """
    Pydantic model for creating a new user.
    Includes validation for email and name fields.
    Attributes:
        - name: User's first name (must contain only letters and spaces)
        - lastname: User's last name (must contain only letters and spaces)
        - username: User's username
        - email: User's email (must be a valid gmail.com address)
    """
    name: str
    lastname: str
    username: str
    email: str

    @classmethod
    def parse_email(cls, email):
        """
        Helper method to parse email into domain components.
        Returns the domain parts after splitting at '@' and '.'
        """
        
        try :
            parsed_email = email.split("@")
            if len(parsed_email) != 2 :
               raise ValidationException("Invalid email")
            parsed_email_result = parsed_email[1].split(".")
            return parsed_email_result
        except ValidationException as e :
            raise HTTPException(status_code=400, detail=str(e))

        

    @field_validator("email")
    def email_must_be_valid(cls, email):
        """
        Validates that the email is a valid gmail.com address.
        Raises HTTP 400 error if email format is invalid.
        """
        parsed_email = cls.parse_email(email)
        
        try:
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
    def valid_name(cls, name: str):
        """
        Validates that the name contains only letters and spaces.
        Raises HTTP 422 error if name contains invalid characters.
        """
        for letter in name:
            if not letter.isalpha() and not letter.isspace():
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail="Su nombre no es valido , contiene caracteres que no son letras"
                )
        return name
    
    @field_validator("lastname")
    def valid_lastname(cls, lastname: str):
        """
        Validates that the lastname contains only letters and spaces.
        Raises HTTP 422 error if lastname contains invalid characters.
        """
        for letter in lastname:
            if not letter.isalpha() and not letter.isspace():
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    detail="Su apellido no es valido , contiene caracteres que no son letras"
                )
        return lastname
        

class UserModel(BaseModel):
    """
    Pydantic model for representing a complete user record.
    Used for responses and data serialization.
    Attributes:
        - id: UUID identifier for the user
        - name: User's first name
        - lastname: User's last name
        - username: User's username
        - email: User's email
        - hashed_password: User's encrypted password
        - roles: List of assigned roles
        - type: User type identifier
    """
    id: uuid.UUID
    name: str
    lastname: str
    username: str
    email: str
    hashed_password: str 
    roles: list[str] | None = None
    type: str

class UserLoginModel(BaseModel):
    """
    Pydantic model for user login requests.
    Attributes:
        - email: User's email
        - password: User's password (plain text for validation)
    """
    email: str
    password: str
