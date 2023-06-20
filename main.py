import asyncio 
import uvicorn
from src.utils.db import create_db


# if __name__ == "__main__":
#     uvicorn.run("src:app",reload=True)

asyncio.run(create_db())