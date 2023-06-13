import asyncio
from .connect import engine
from .models import Base,Note,NoteBook

import logging


async def create_db():
    async with engine.begin() as conn:
        try:
            from .models import Note, NoteBook,User

            await conn.run_sync(Base.metadata.create_all)
            

        except Exception as e:
            print(e)
            

    await engine.dispose()

# asyncio.run(create_db())