from pydantic import BaseModel,Field

class SignUpSchema(BaseModel):
    username: str = Field(max_length=50)
    email : str = Field(max_length=80)
    password : str = Field(min_length=6)

    class Config:
        orm_mode = True


class SignUpResponse(BaseModel):
    username : str
    email: str