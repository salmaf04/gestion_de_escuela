from fastapi import FastAPI, HTTPException, status, Depends
from .schemas import UserCreateModel, UserModel, UserLoginModel
from sqlalchemy.orm import Session
from .services import UserCreateService
from fastapi.exceptions import HTTPException
from .utils import verify_password, create_access_token
from datetime import timedelta
from fastapi.responses import JSONResponse
from database.config import SessionLocal, engine
from database import tables
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/otro"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
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

EXPIRE_TOKEN=2

@app.get("/")
async def say_hello() :
    return {
        "message" : "Welcome"
    }

@app.post(
    "/signup",
    status_code=status.HTTP_201_CREATED
)
async def create_user_account(
    user_input: UserCreateModel,
    session: Session = Depends(get_db)
) :
    user_service=UserCreateService()

    user_exists = await user_service.user_exists(email=user_input.email, session=session)

    if user_exists :
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "There is already an user with that email"
        )
    
    return await user_service.create_user(user=user_input, session=session)


@app.post(
    '/login',
)
async def user_loggin(
    login_data: UserLoginModel,
    session: Session = Depends(get_db)
) :# Depends(get_session)) 

    user_service=UserCreateService()

    user = await user_service.get_user_by_email(email=login_data.email, session=session)

    if user is None :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Email not found'
        )
    
    password = login_data.password

    if verify_password(password, user.hashed_password) :
        access_token =  create_access_token(
            user_data ={
                'email': user.email,
                'user_id': str(user.id)
            }
        )

        refresh_token =  create_access_token(
            user_data ={
                'email': user.email,
                'user_id': str(user.id)
            },
            refresh=True,
            expire=timedelta(days=EXPIRE_TOKEN)
        )

        return JSONResponse(
            content={
                "message":"Loggin succesfull",
                "access_token":access_token,
                "resfresh-token":refresh_token,
                "user_data" : {
                    "email" : user.email,
                    "id" : str(user.id)
                }

            }
        )
    
    return HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid Credentials"
    )
            

        




    