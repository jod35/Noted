from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker
from ..db.models import User
from sqlalchemy import select



async def add_user(async_session:async_sessionmaker[AsyncSession],userObj:User):
    async with async_session() as session:
        async with session.begin():
            session.add(userObj)
            session.commit()


async def get_user(async_session:async_sessionmaker[AsyncSession],user_id):
    async with async_session() as session:
        statement = select(User).where(User.id==id)

        user = session.scalars(statement).one()

        return user


