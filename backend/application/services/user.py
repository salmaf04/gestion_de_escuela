from sqlalchemy.orm import Session
from sqlalchemy import select, update
from backend.domain.models.tables import UserTable
from backend.domain.schemas.user import UserCreateModel, UserModel
from ..utils.auth import get_password_hash
from backend.application.utils.auth import verify_password
from backend.domain.filters.user import UserChangeRequest, UserPasswordChangeRequest, UserFilterSchema, UserFilterSet
from fastapi import HTTPException
from backend.infrastructure.repositories.user import UserRepository

class UserCreateService:
    def __init__(self, session):
        self.repo_instance = UserRepository(session)

    async def create_user(self, user: UserCreateModel) :
        return self.repo_instance.create(user)

    async def get_user_by_username(self, username: str) -> UserModel :
        return self.repo_instance.get_user_by_username(username)
        
    async def get_user_by_id(self, id: str) -> UserModel :
        return self.repo_instance.get_by_id(id)
        
    async def user_exists(self, username: str) :
        return self.repo_instance.user_exists(username)
    
class UserUpdateService:
    def __init__(self, session):
        self.repo_instance = UserRepository(session)

    async def update_user(
        self, 
        user_input: UserModel,
        password_change_request: UserPasswordChangeRequest=None,
        personal_info_change_request: UserChangeRequest=None,
    ): 
       return await self.repo_instance.update(user_input, password_change_request, personal_info_change_request)
    
class UserPaginationService :
    def __init__(self, session):
        self.repo_instance = UserRepository(session)

    def get_user(self, filter_params: UserFilterSchema) -> list[UserTable] :
        return self.repo_instance.get(filter_params)



            
    
  
    