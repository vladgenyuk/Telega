from sqlalchemy import insert, select

from database import async_session
from models import User


class UserCRUD:
    @staticmethod
    async def add_user(username: str, email: str):
        async with async_session() as session:
            stmt = insert(User).values(username=username, email=email)
            await session.execute(stmt)
            await session.commit()

    @staticmethod
    async def user_exists(email: str):
        async with async_session() as session:
            stmt = select(User).where(User.email == email)
            user = await session.execute(stmt)
            user = [dict(i._mapping) for i in user]
        if user:
            return True
        return False
