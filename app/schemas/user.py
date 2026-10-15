from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl


class UserDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str = Field(min_length=2, max_length=30)
    about: str = Field(min_length=2, max_length=200)
    avatar: HttpUrl | None = None
    email: EmailStr


class UpdateUserDTO(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=30)
    about: str | None = Field(default=None, min_length=2, max_length=200)
    avatar: HttpUrl | None = None


class UpdateAvatarDTO(BaseModel):
    avatar: str


class CreateUserDTO(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    name: str = Field(min_length=2, max_length=30)
    about: str = Field(min_length=2, max_length=200)
    avatar: HttpUrl | None = None


#   name: {
#     type: String,
#     required: false,
#     minlength: 2,
#     maxlength: 30,
#   },
#   about: {
#     type: String,
#     required: false,
#     minlength: 2,
#     maxlength: 200,
#   },
#   avatar: {
#     type: String,
#     required: false,
#   },
#   email: {
#     type: String,
#     required: true,
#     unique: true,
#   },
#   password: {
#     type: String,
#     required: true,
#     select: false,
#   },
