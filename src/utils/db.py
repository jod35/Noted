from ..api.db.base import engine,Base

async def create_db():
    async with engine.begin() as conn:
        from ..api.auth.models import User
        from ..api.notebooks.models import NoteBook
        from ..api.notes.models import Note
        print("Creating DB>>>>>")
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
            
    await engine.dispose()