## authorizations.py
from functools import wraps
from fastapi import HTTPException, status
# authentications
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt import PyJWTError
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta, timezone
import json
from backend.application.services.user import UserCreateService
from backend.domain.models.tables import UserTable
from backend.domain.models import tables
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from backend.application.serializers.user import UserMapper
from backend.configuration import get_db

"""
This module provides authorization and authentication functionalities for a FastAPI application.

Functions:
    authenticate_user: Authenticates a user by verifying their username and password.
    create_access_token: Creates a JWT access token with an optional expiration time.
    get_current_user: Retrieves the current user based on the provided JWT token.
    verify_password: Verifies a plain password against a hashed password.
    authorize: A decorator to enforce role-based access control on API endpoints.
    parse_url: Parses a URL to extract the endpoint path.

Constants:
    SECRET_KEY: The secret key used for encoding and decoding JWT tokens.
    ALGORITHM: The algorithm used for encoding JWT tokens.
    ACCESS_TOKEN_EXPIRE_MINUTES: The default expiration time for access tokens in minutes.

Dependencies:
    - FastAPI for building the web application and handling HTTP exceptions.
    - JWT for encoding and decoding JSON Web Tokens.
    - Passlib for password hashing and verification.
    - SQLAlchemy for database interactions.
    - UserCreateService and UserMapper for user-related operations.
    - OAuth2PasswordBearer for token-based authentication.

Usage:
    - Use `authenticate_user` to verify user credentials during login.
    - Use `create_access_token` to generate a JWT token for authenticated users.
    - Use `get_current_user` as a dependency to retrieve the current user in protected routes.
    - Use `authorize` as a decorator to restrict access to certain roles.
    - Use `parse_url` to extract the endpoint path from a URL.
"""

# Define OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# JWT token related constants
SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Authenticate user
async def authenticate_user(username: str, password: str, session: Session):
    user_service = UserCreateService(session)  
    mapper = UserMapper()
    user = await user_service.get_user_by_username(username=username)

    if user is None :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario Incorrecto"
        )
    
    user = mapper.to_api(user)

    if  not verify_password(password, user.hashed_password):
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña Incorrecta"
        )

    return user

# Create access token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependency to get current user based on token
async def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_db)):
    try :
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        user_service = UserCreateService(session)  
        user = user_service.get_user_by_id(id=user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No existe ningun usuario con ese identificador"
            )
        return user
    except Exception as e :
        return {f"{e}"}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authorize(role: list):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            user =  await kwargs.get("current_user")
            user_id1 = user.id
            user_roles = user.roles
            check_id =  kwargs.get("id", None)
        
            if kwargs.get("request") is not None:
                request = kwargs.get("request")
                method = request.method
                url = parse_url(request.url.path)
                throw_unauthorized = True

                if method == 'GET' and url == 'student' :
                    if 'teacher' in user_roles :
                        kwargs['students_by_teacher'] = True
                        kwargs['teacher_id'] = user_id1

                if method == 'GET' and url == 'teacher':
                    if 'student' in user_roles :
                        kwargs['teachers_by_students'] = True
                        kwargs['student_id'] = user_id1

                if method == 'GET' and url == 'absence':
                    if 'student' in user_roles :
                        kwargs['by_student'] = user_id1
                    elif 'teacher' in user_roles :
                        kwargs['by_student_by_teacher'] = user_id1

                if method == 'GET' and url == 'subject':
                    if 'student' in user_roles :
                        kwargs['subjects_by_students'] = user_id1
                    elif 'teacher' in user_roles :
                        kwargs['subjects_by_teacher'] = user_id1

                if method == 'GET' and url == 'note':
                    if 'student' in user_roles :
                        kwargs['by_student'] = user_id1
                    elif 'teacher' in user_roles :
                        kwargs['by_teacher'] = user_id1
                
                if (method == 'PATCH' or method == 'POST') and url == 'note':
                    kwargs['user_id']=user_id1

                if method == 'PATCH' and url == 'user':
                    if check_id and check_id != str(user_id1):
                        raise HTTPException(status_code=403, detail="Usted solo tiene permitido modificar su propio perfil")
                
            for role in user_roles :
                if role in role :
                    throw_unauthorized = False
            
            if throw_unauthorized :
                for role in user_roles :
                    role_str = ','.join(role)
                    raise HTTPException(status_code=403, detail=f"User is not authorized to access , only avaliable for {role_str}")
            
            return await func(*args, **kwargs)
        return wrapper
    return decorator

def parse_url(url:str):
    return url.split('/')[1]







