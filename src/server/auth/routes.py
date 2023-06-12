from fastapi import APIRouter


auth_router = APIRouter(tags=["auth"])

@auth_router.get("/")
async def hello():
    return {"message":"Hello Auth"}