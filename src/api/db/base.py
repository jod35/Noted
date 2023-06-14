from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker


engine = create_async_engine(
    "postgresql+asyncpg://postgresql:nathanoj35@localhost/notes_app",
    echo=True
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False
)