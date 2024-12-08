from sqlalchemy.orm import Session
from sqlalchemy import select
from domain.models.tables import UserTable
from domain.schemas.user import UserCreateModel, UserModel
from utils.auth import get_password_hash


class UserCreateService:
    async def get_user_by_username(self, username: str, session: Session) -> UserModel :
        query = select(UserTable).where(UserTable.username == username)

        result =  session.execute(query)

        user = result.scalars().first()
    
    
        return  UserModel(
            id = user.entity_id,
            email=user.email,
            username=user.username,
            hashed_password=user.hash_password,
            type=user.type
        )
    

    async def user_exists(self, username: str, session: Session) :
        user = await self.get_user_by_username(username=username, session=session)

        return user is not None
    
    
    async def create_user(self, user: UserCreateModel, session: Session) :
        user_dict = user.model_dump()

        hashed_password = get_password_hash(user.password)

        new_user = UserTable(**user_dict, hash_password=hashed_password)

        session.add(new_user)

        session.commit()

        return UserModel(
            id = new_user.entity_id,
            email=new_user.email,
            username=new_user.username,
            hashed_password=new_user.hash_password,
            type=new_user.type
        )