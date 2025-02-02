from sqlalchemy.orm import Session
from sqlalchemy import select, update
from backend.domain.models.tables import UserTable
from backend.domain.schemas.user import UserCreateModel, UserModel
from ..utils.auth import get_password_hash
from backend.application.utils.auth import verify_password
from backend.domain.filters.user import UserChangeRequest, UserPasswordChangeRequest, UserFilterSchema, UserFilterSet
from fastapi import HTTPException

class UserCreateService:
    async def get_user_by_username(self, username: str, session: Session) -> UserModel :
        query = select(UserTable).where(UserTable.username == username)

        result =  session.execute(query)

        user = result.scalars().first()
    
        return user
    
    async def get_user_by_id(self, id: str, session: Session) -> UserModel :
        query = select(UserTable).where(UserTable.entity_id == id)

        result =  session.execute(query)

        user = result.scalars().first()
    
        return user
        
    
    async def user_exists(self, username: str, session: Session) :
        user = await self.get_user_by_username(username=username, session=session)

        return user is not None
    
    
    async def create_user(self, user: UserCreateModel, session: Session) :
        user_dict = user.model_dump()

        hashed_password = get_password_hash(user.password)

        new_user = UserTable(**user_dict, hash_password=hashed_password)

        session.add(new_user)

        session.commit()

        return new_user
    
class UserUpdateService:
    async def update_user(
        self, 
        session: Session,
        user_input: UserModel,
        password_change_request: UserPasswordChangeRequest=None,
        personal_info_change_request: UserChangeRequest=None,
    ): 
        if password_change_request :
            user_input_new = await self.update_password(password_change_request=password_change_request, user_input=user_input, session=session)
        if personal_info_change_request :
            user_input_new = await self.update_personal_info(personal_info_change_request=personal_info_change_request, user_input=user_input, session=session)
        
        user_update = user_input_new.model_dump(exclude={'id'})
        print(user_update)
        query = update(UserTable)
        query = query.where(UserTable.entity_id == user_input.id)
        query = query.values(user_update)
        session.execute(query)
        session.commit()
       
        return user_input_new
    
    async def update_password(self, password_change_request: UserPasswordChangeRequest, user_input: UserModel, session: Session):
        if password_change_request.current_password :
           if not verify_password(password_change_request.current_password, user_input.hashed_password) :
               raise HTTPException(status_code=400, detail="Invalid current password")
           
           new_hashed_password = get_password_hash(password_change_request.new_password)
           user_input.hashed_password = new_hashed_password
           return user_input
        
    async def update_personal_info(self, personal_info_change_request: UserChangeRequest, user_input: UserModel, session: Session):
        if personal_info_change_request.username :
            user_input.username = personal_info_change_request.username
        
        if personal_info_change_request.email :
            user_input.email = personal_info_change_request.email

        return user_input
    

class UserPaginationService :
    def get_user(self, session: Session, filter_params: UserFilterSchema) -> list[UserTable] :
        query = select(UserTable)
        filter_set = UserFilterSet(session, query=query)
        query = filter_set.filter_query(filter_params.model_dump(exclude_unset=True,exclude_none=True))
        return session.execute(query).scalars().all()


            
    
  
    