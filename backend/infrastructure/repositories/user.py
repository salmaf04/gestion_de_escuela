from sqlalchemy import update, select
from backend.domain.models.tables import UserTable
from backend.domain.schemas.user import UserCreateModel, UserModel
from backend.application.utils.auth import get_password_hash
from backend.application.utils.auth import verify_password
from backend.domain.filters.user import UserChangeRequest, UserPasswordChangeRequest, UserFilterSchema, UserFilterSet
from fastapi import HTTPException
from .base import IRepository

class UserRepository(IRepository[UserCreateModel,UserTable, UserChangeRequest,UserFilterSchema]):
    """
    Repository for managing users in the database.
    Extends IRepository with specific implementations for user operations.
    """
    def __init__(self, session):
        """Initialize repository with database session."""
        super().__init__(session)

    def create(self, entity: UserCreateModel) -> UserTable:
        """
        Create a new user record with hashed password.
        Args:
            entity: UserCreateModel containing user details
        Returns:
            Created UserTable instance
        """
        user_dict = entity.model_dump()
        hashed_password = get_password_hash(entity.password)
        new_user = UserTable(**user_dict, hash_password=hashed_password)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def delete(self, entity: UserTable) -> None:
        """Delete a user from the database."""
        self.session.delete(entity)
        self.session.commit()

    def get_by_id(self, id: str) -> UserTable:
        """Retrieve a user by their ID."""
        query = self.session.query(UserTable).filter(UserTable.entity_id == id)
        result = query.scalar()
        return result
    
    def get(self, filter_params: UserFilterSchema) -> list[UserTable]:
        """Get users based on filter parameters."""
        query = select(UserTable)
        filter_set = UserFilterSet(self.session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return self.session.execute(query).scalars().all()
    
    async def update(
        self, 
        entity: UserModel,
        password_change_request: UserPasswordChangeRequest=None,
        personal_info_change_request: UserChangeRequest=None,    
    ):
        """
        Update user information and/or password.
        Args:
            entity: Current UserModel to be updated
            password_change_request: Optional password change details
            personal_info_change_request: Optional personal info change details
        Returns:
            Updated UserModel instance
        """
        if password_change_request:
            user_input_new = await self.update_password(password_change_request=password_change_request, user_input=entity)
        if personal_info_change_request :
            user_input_new = await self.update_personal_info(personal_info_change_request=personal_info_change_request, user_input=entity)
    
        user_update = user_input_new.model_dump(exclude={'id'})
        query = update(UserTable)
        query = query.where(UserTable.entity_id == entity.id)
        query = query.values(user_update)
        self.session.execute(query)
        self.session.commit()
        return user_input_new
    
    async def update_password(self, password_change_request: UserPasswordChangeRequest, user_input: UserModel):
        """
        Update user's password after verifying current password.
        Raises HTTPException if current password is invalid.
        """
        if password_change_request.current_password:
           if not verify_password(password_change_request.current_password, user_input.hashed_password):
               raise HTTPException(status_code=400, detail="Invalid current password")
           
           new_hashed_password = get_password_hash(password_change_request.new_password)
           user_input.hashed_password = new_hashed_password
           return user_input
        
    async def update_personal_info(self, personal_info_change_request: UserChangeRequest, user_input: UserModel):
        """Update user's personal information (username and/or email)."""
        if personal_info_change_request.username:
            user_input.username = personal_info_change_request.username
        
        if personal_info_change_request.email:
            user_input.email = personal_info_change_request.email

        if personal_info_change_request.name:
            user_input.name = personal_info_change_request.name
        
        if personal_info_change_request.lastname:    
            user_input.lastname = personal_info_change_request.lastname
            
        return user_input

    def get_user_by_username(self, username: str) -> UserModel:
        """
        Retrieve a user by their username.
        Args:
            username: Username to search for
        Returns:
            Matching UserModel instance or None
        """
        query = select(UserTable).where(UserTable.username == username)
        result = self.session.execute(query)
        user = result.scalars().first()
        return user
    
    def user_exists(self, username: str) -> bool:
        """
        Check if a user with the given username exists.
        Args:
            username: Username to check
        Returns:
            Boolean indicating if user exists
        """
        user = self.get_user_by_username(username=username)
        return user is not None
    
    



            