from sqlalchemy.orm import Session
from sqlalchemy import select, update
from backend.domain.models.tables import UserTable
from backend.domain.schemas.user import UserCreateModel, UserModel
from ..utils.auth import get_password_hash
from backend.application.utils.auth import verify_password
from backend.domain.filters.user import UserChangeRequest, UserPasswordChangeRequest, UserFilterSchema, UserFilterSet
from fastapi import HTTPException
from backend.infrastructure.repositories.user import UserRepository

"""
This module defines services for creating, retrieving, updating, and managing user records.

Classes:
    UserCreateService: A service for creating new user records and retrieving user information.
    UserUpdateService: A service for updating user records.
    UserPaginationService: A service for retrieving user records based on various criteria.

Classes Details:

1. UserCreateService:
    - This service is responsible for creating new user records and retrieving user information.
    - It utilizes the UserRepository to interact with the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - create_user(user: UserCreateModel): 
            Asynchronously creates a new user record using the provided UserCreateModel.
        - get_user_by_username(username: str) -> UserModel: 
            Asynchronously retrieves a user record by the specified username.
        - get_user_by_id(id: str) -> UserModel: 
            Asynchronously retrieves a user record by the specified ID.
        - user_exists(username: str): 
            Asynchronously checks if a user with the specified username exists.

2. UserUpdateService:
    - This service is responsible for updating user records.
    - It uses the UserRepository to perform update operations.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - update_user(user_input: UserModel, password_change_request: UserPasswordChangeRequest=None, personal_info_change_request: UserChangeRequest=None): 
            Asynchronously updates the specified user record with the provided changes.

3. UserPaginationService:
    - This service is responsible for retrieving user records based on different criteria.
    - It uses the UserRepository to fetch data from the database.
    
    Methods:
        - __init__(session): Initializes the service with a database session.
        - get_user(filter_params: UserFilterSchema) -> list[UserTable]: 
            Retrieves a list of users based on the provided filter parameters.

Dependencies:
    - SQLAlchemy ORM for database interactions.
    - UserRepository for database operations related to users.
    - UserCreateModel, UserModel, UserTable, and other domain models for data representation.
    - UserFilterSchema and UserFilterSet for filtering user records.
    - Utility functions for password hashing and verification.
    - FastAPI for handling HTTP exceptions.
"""

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



            
    
  
    