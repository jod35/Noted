import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from .base import engine



async def connect():
    async with engine.begin() as conn:
        await conn.execute(text("select 'Hello'"))

    
    await engine.dispose()

