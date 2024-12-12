## authorizations.py
from functools import wraps
from fastapi import HTTPException
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

import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")


engine = create_engine(
    database_url
)

tables.BaseTable.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# JWT token related constants
SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Authenticate user
async def authenticate_user(username: str, password: str, session: Session):
    user_service = UserCreateService()  
    mapper = UserMapper()
    user = await user_service.get_user_by_username(username=username, session=session)
    if user is None :
        return None
    
    user = mapper.to_api(user)

    if  not verify_password(password, user.hashed_password):
        return None

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
    payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")
    user_service = UserCreateService()  
    user = user_service.get_user_by_username(username=username, session=session)
    if user is None:
        return None
    return user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authorize(role: list):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            user =  await kwargs.get("current_user")
            filters =  kwargs.get("filters")
            user_role = user.type    
            if user_role not in role:
                role_str = ','.join(role)
                raise HTTPException(status_code=403, detail=f"User is not authorized to access , only avaliable for {role_str}")
            if filters and filters.hash_password and user_role == "secretary" :
                raise HTTPException(status_code=403, detail=f"User is not authorized to access , only avaliable for {role[1]}")

            return await func(*args, **kwargs)
        return wrapper
    return decorator