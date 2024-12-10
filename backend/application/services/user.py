from sqlalchemy.orm import Session
from sqlalchemy import select
from backend.domain.models.tables import UserTable
from backend.domain.schemas.user import UserCreateModel, UserModel
from ..utils.auth import get_password_hash


class UserCreateService:
    async def get_user_by_username(self, username: str, session: Session) -> UserModel :
        query = select(UserTable).where(UserTable.username == username)

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