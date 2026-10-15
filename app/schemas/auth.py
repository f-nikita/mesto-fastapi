from pydantic import BaseModel, EmailStr, Field


class LoginDTO(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class TokenDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"
