from fastapi import APIRouter


notes_router = APIRouter(tags=["notes"])

@notes_router.get('/')
async def hello():
    return {"message":"Hello World"}