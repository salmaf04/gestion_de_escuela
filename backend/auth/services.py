from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import select
from ..database.tables import User
from schemas import UserModel
from schemas import UserCreateModel
from utils import generate_password_hash


class UserCreateService:
    async def get_user_by_email(self, email: str, session: AsyncSession) -> UserModel :
        query = select(User).where(User.email == email)

        result = await session.execute(query)

        user = result.first()
        
        return user
    

    async def user_exists(self, email:str, session: AsyncSession) :
        user = await self.get_user_by_email(email=email, session=session)

        return user is not None
    
    
    async def create_user(self, user: UserCreateModel, session: AsyncSession) :
        user_dict = user.model_dump()

        new_user = User(**user_dict)

        new_user.hash_password = generate_password_hash(user_dict.get("password"))

        session.add(new_user)

        await session.commit()

        return new_user