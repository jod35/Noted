from fastapi import APIRouter

notebook_router = APIRouter(
    tags=["notebooks"]
)


@notebook_router.get("/")
def hello():
    return {"message":"Hello notebooks"}