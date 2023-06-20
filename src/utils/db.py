from ..api.db.base import async_session,engine


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync()
            
