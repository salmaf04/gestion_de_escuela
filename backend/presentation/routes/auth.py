## main.py
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta
from ..utils.auth import authorize , get_current_user, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from backend.application.services.user import UserCreateService
from backend.domain.models import tables
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from backend.domain.schemas.user import UserCreateModel, UserModel
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")


engine = create_engine(
    database_url
)

tables.BaseTable.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define endpoints for token generation and authentication
@router.post(
    "/token",
    response_model=dict,
    status_code=status.HTTP_200_OK
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    user = await authenticate_user(form_data.username, form_data.password, session)

    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "sub": user.username,
            "type": user.type
        }, 
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


# Define a route for registering a new user
@router.post(
    "/register",
    response_model=UserModel,
    status_code=status.HTTP_201_CREATED
)
async def register_user(user: UserCreateModel, session: Session = Depends(get_db)):
    user_service = UserCreateService()

    if await user_service.user_exists(user.username, session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    created_user = await user_service.create_user(user=user, session=session)
    return created_user

    
@router.get("/check-all")
@authorize(role=['superadmin'])
async def route1(current_user: UserModel = Depends(get_current_user)):
    return {"message": "This endpoint is accessible to admin and superadmin only"}


@router.get("/check-superadmin")
@authorize(role=['superadmin'])
async def route2(current_user: UserModel = Depends(get_current_user)):
    return {"message": "This endpoint is accessible to superadmin only"}

        




    