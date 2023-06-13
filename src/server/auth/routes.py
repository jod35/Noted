from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from ...schemas.accounts import SignUpSchema,SignUpResponse
from ...utils.passwords import generate_pwd_hash,check_password
from ...db.models import User
from ...db.base import async_session

auth_router = APIRouter(tags=["auth"])
session = async_session()

@auth_router.get("/")
async def hello():
    return {"message":"Hello Auth"}


@auth_router.post("/signup",response_model=SignUpResponse)
async def create_user_account(user:SignUpSchema):
    """
    Create a user account using username, email, password
    """

    try:
        new_user = User(
            username = user.username,
            email=user.email,
            password_hash = generate_pwd_hash(user.password)
        )
        await session.add(new_user)
        await session.commit()
        return {"message":"User Created Successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400,detail="error occured")

