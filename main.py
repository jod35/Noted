import asyncio 
import uvicorn


if __name__ == "__main__":
    uvicorn.run("src:app",reload=True)

# asyncio.run(create_db())