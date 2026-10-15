from pydantic import BaseModel


class UserDTO(BaseModel):
    id: str
    name: str
    about: str
    avatar: str | None = None


class UpdateUserDTO(BaseModel):
    name: str | None = None
    about: str | None = None
    avatar: str | None = None


class UpdateAvatarDTO(BaseModel):
    avatar: str
