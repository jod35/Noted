from sqlalchemy.ext.asyncio import create_async_engine
from ..settings import DATABASE_URL

#engine
engine = create_async_engine(
    DATABASE_URL,
    echo =True
)