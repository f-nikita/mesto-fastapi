from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    about: str
    avatar: str | None = None


class UpdateUser(BaseModel):
    name: str | None = None
    about: str | None = None
    avatar: str | None = None


class UpdateAvatar(BaseModel):
    avatar: str
