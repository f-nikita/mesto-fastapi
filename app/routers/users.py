from fastapi import APIRouter

from app.constants import USER_IS_NOT_DEFINED
from app.schemas.user import UpdateAvatar, UpdateUser, User
from app.services import users as user_services

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[User])
async def get_all_users():
    return user_services.get_all_users()


@router.get(
    "/me",
    response_model=User,
    responses={404: {"description": USER_IS_NOT_DEFINED}},
)
async def get_profile():
    return user_services.get_profile()


@router.get(
    "/{user_id}",
    response_model=User,
    responses={404: {"description": USER_IS_NOT_DEFINED}},
)
async def get_profile_by_id(user_id: str):
    return user_services.get_profile_by_id(user_id)


@router.patch(
    "/me",
    response_model=UpdateUser,
    responses={404: {"description": USER_IS_NOT_DEFINED}},
)
async def update_profile(update_data: UpdateUser):
    return user_services.update_profile(update_data)


@router.patch(
    "/me/avatar",
    response_model=UpdateUser,
    responses={404: {"description": USER_IS_NOT_DEFINED}},
)
async def update_profile_avatar(update_data: UpdateAvatar):
    return user_services.update_profile_avatar(update_data)
