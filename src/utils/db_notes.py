from ..db.models import Note,NoteBook
from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker
from sqlalchemy import select,text



async def add_note(async_session:async_sessionmaker[AsyncSession],noteObj:Note):
    async with async_session() as session:
        async with session.begin():
            session.add(noteObj)
            session.commit()


async def get_note(async_session:async_sessionmaker[AsyncSession],id):
    async with async_session() as session:
        stmt = select(Note).where(Note.id==id)
        result = session.scalars(stmt).one()
        return result
    

async def get_all_notes(async_session:async_sessionmaker[AsyncSession]):
    async with async_session() as session:
        stmt = text("select * from notes")
        result= session.execute(stmt)
        return result

