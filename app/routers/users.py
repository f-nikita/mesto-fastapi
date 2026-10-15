from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.constants import USER_IS_NOT_DEFINED
from app.database import get_session
from app.dependencies import get_current_user
from app.models.user import UserModel
from app.schemas.user import UpdateAvatarDTO, UpdateUserDTO, UserDTO
from app.services import users as user_services

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[UserDTO])
async def get_all_users(
    session: Annotated[AsyncSession, Depends(get_session)],
):
    return await user_services.get_all_users(session)


@router.get(
    "/me",
    response_model=UserDTO,
    responses={401: {"description": "Не авторизован"}},
)
async def get_profile(
    current_user: Annotated[UserModel, Depends(get_current_user)],
):
    return current_user


@router.get(
    "/{user_id}",
    response_model=UserDTO,
    responses={401: {"description": USER_IS_NOT_DEFINED}},
)
async def get_profile_by_id(
    user_id: UUID,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    return await user_services.get_profile_by_id(user_id, session)


@router.patch(
    "/me",
    response_model=UserDTO,
    responses={401: {"description": "Не авторизован"}},
)
async def update_profile(
    update_data: UpdateUserDTO,
    current_user: Annotated[UserModel, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    return await user_services.update_profile(
        current_user,
        update_data,
        session,
    )


@router.patch(
    "/me/avatar",
    response_model=UpdateAvatarDTO,
    responses={401: {"description": USER_IS_NOT_DEFINED}},
)
async def update_profile_avatar(
    update_avatar: UpdateAvatarDTO,
    current_user: Annotated[UserModel, Depends(get_current_user)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    return await user_services.update_profile_avatar(
        update_avatar, current_user, session
    )
