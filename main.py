import asyncio 
from src.db.create_db import create_db
import uvicorn
import uvicorn



if __name__ == "__main__":
    uvicorn.run("src:app",reload=True)