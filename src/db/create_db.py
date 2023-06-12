import asyncio
from .connect import engine
from .models import Base,Note,NoteBook

import logging


async def create_db():
    async with engine.begin() as conn:
        try:
            from .models import Note, NoteBook
            await conn.run_sync(Base.metadata.drop_all)
            

        except Exception as e:
            print(e)
            

    await engine.dispose()

