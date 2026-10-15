from fastapi import APIRouter

from app.constants import USER_IS_NOT_DEFINED
from app.schemas.user import UpdateAvatarDTO, UpdateUserDTO, UserDTO
from app.services import users as user_services

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[UserDTO])
async def get_all_users():
    return user_services.get_all_users()


@router.get(
    "/me",
    response_model=UserDTO,
    responses={404: {"description": USER_IS_NOT_DEFINED}},
)
async def get_profile():
    return user_services.get_profile()


@router.get(
    "/{user_id}",
    response_model=UserDTO,
    responses={404: {"description": USER_IS_NOT_DEFINED}},
)
async def get_profile_by_id(user_id: str):
    return user_services.get_profile_by_id(user_id)


@router.patch(
    "/me",
    response_model=UserDTO,
    responses={404: {"description": USER_IS_NOT_DEFINED}},
)
async def update_profile(update_data: UpdateUserDTO):
    return user_services.update_profile(update_data)


@router.patch(
    "/me/avatar",
    response_model=UpdateAvatarDTO,
    responses={404: {"description": USER_IS_NOT_DEFINED}},
)
async def update_profile_avatar(update_data: UpdateAvatarDTO):
    return user_services.update_profile_avatar(update_data)
