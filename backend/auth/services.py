from sqlalchemy.orm import Session
from sqlalchemy import select
from database.tables import UserTable
from .schemas import UserModel
from .schemas import UserCreateModel
from .utils import generate_password_hash


class UserCreateService:
    async def get_user_by_email(self, email: str, session: Session) -> UserModel :
        query = select(UserTable).where(UserTable.email == email)

        result = session.scalars(query)

        user = result.first()
    
        return  UserModel(
            id = user.entity_id,
            email=user.email,
            username=user.username,
            hashed_password=user.hash_password
        )
    

    async def user_exists(self, email:str, session: Session) :
        user = await self.get_user_by_email(email=email, session=session)

        return user is not None
    
    
    async def create_user(self, user: UserCreateModel, session: Session) :
        user_dict = user.model_dump()

        hashed_password = generate_password_hash(user.password)

        new_user = UserTable(**user_dict, hash_password=hashed_password)

        session.add(new_user)

        session.commit()

        return UserModel(
            id = new_user.entity_id,
            email=new_user.email,
            username=new_user.username,
            hashed_password=new_user.hash_password
        )