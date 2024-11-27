from fastapi import APIRouter, HTTPException, status, Depends
from schemas import UserCreateModel, UserModel, UserLoginModel
from sqlalchemy.ext.asyncio import AsyncSession
from services import UserCreateService
from fastapi.exceptions import HTTPException
from utils import verify_password, create_access_token
from datetime import timedelta
from fastapi.responses import JSONResponse

app = APIRouter()
EXPIRE_TOKEN='2'

@app.post(
    "/signup",
    response_model=UserModel,
    status_code=status.HTTP_201_CREATED
)
async def create_user_account(
    user_input: UserCreateModel,
    session: AsyncSession
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
    session:AsyncSession 
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
                'user_id': user.id,
            }
        )

        refresh_token =  create_access_token(
            user_data ={
                'email': user.email,
                'user_id': user.id,
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
            

        




    