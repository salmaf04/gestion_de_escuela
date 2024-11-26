from fastapi import APIRouter, HTTPException, status
from schemas import UserCreateModel, UserModel
from sqlalchemy.ext.asyncio import AsyncSession
from services import UserService
from fastapi.exceptions import HTTPException

app = APIRouter()

@app.post(
    "/signup",
    response_model=UserModel,
    status_code=status.HTTP_201_CREATED
)
async def create_user_account(
    user_input: UserCreateModel,
    session: AsyncSession
) :
    user_service=UserService()

    user_exists = await user_service.user_exists(email=user_input.email, session=session)

    if user_exists :
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "There is already an user with that email"
        )
    
    return await user_service.create_user(user=user_input, session=session)

    