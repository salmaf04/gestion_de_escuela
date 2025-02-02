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







