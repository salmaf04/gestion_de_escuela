## main.py
from fastapi import APIRouter, HTTPException, Depends, status, Body, Header
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta

from backend.application.serializers.user import UserMapper
from ..utils.auth import authorize , get_current_user, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from backend.application.services.user import UserCreateService, UserUpdateService
from sqlalchemy.orm import Session
from backend.domain.schemas.user import UserCreateModel, UserModel
from backend.configuration import get_db
from backend.domain.filters.user import UserChangeRequest, UserPasswordChangeRequest
from backend.domain.schemas.roles import Roles
from typing import Annotated
from fastapi import Query
from fastapi.requests import Request

roles = Roles.get_roles_list()

router = APIRouter()

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
            "user_id" : str(user.id),
            "type": user.type
        }, 
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post(
    "/logout",
    status_code=status.HTTP_200_OK,
    response_model=dict
)
def user_logout(Authorization: str = Header(None)):
    oauth2_scheme.revoke_token(Authorization)
    return {"message": "Token revoked"} 


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

@router.patch(
       "/user/{id}",
       response_model=UserModel,
       status_code=status.HTTP_200_OK
)
@authorize(roles)
async def update_user(
    request: Request,
    id: str ,
    current_user: UserModel = Depends(get_current_user),
    session: Session = Depends(get_db),
    current_password: Annotated[
        str,
        Body(description="Current password)")  
    ] = None,
    new_password: Annotated[
        str,
        Body(description="Password to update)")  
    ] = None,
    username: Annotated[
        str,
        Body(description="Username to update)")  
    ] = None,
    email: Annotated[
        str,
        Body(description="Email to update)")  
    ] = None,
):
    update_user_service = UserUpdateService()
    create_user = UserCreateService()
    mapper = UserMapper()
    
    password_change_request = UserPasswordChangeRequest(
        current_password=current_password,
        new_password=new_password
    )
    personal_info_change_request = UserChangeRequest(
        username=username,
        email=email
    )
    
    user = await create_user.get_user_by_id(id=id, session=session)
    user = mapper.to_api(user)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    updated_user = await update_user_service.update_user(user_input=user,password_change_request=password_change_request, personal_info_change_request=personal_info_change_request, session=session)

    return updated_user
    

@router.get("/check-all")
@authorize(role=['superadmin'])
async def route1(current_user: UserModel = Depends(get_current_user)):
    return {"message": "This endpoint is accessible to admin and superadmin only"}


@router.get("/check-superadmin")
@authorize(role=['superadmin'])
async def route2(current_user: UserModel = Depends(get_current_user)):
    return {"message": "This endpoint is accessible to superadmin only"}

        




    