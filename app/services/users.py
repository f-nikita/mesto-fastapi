from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.constants import USER_IS_NOT_DEFINED
from app.models.user import UserModel
from app.schemas.user import UpdateAvatarDTO, UpdateUserDTO


async def get_all_users(session: AsyncSession) -> list[UserModel]:
    result = await session.execute(select(UserModel))
    return list(result.scalars().all())


async def get_profile_by_id(user_id: UUID, session: AsyncSession):
    user = await session.get(UserModel, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail=USER_IS_NOT_DEFINED)

    return user


async def update_profile(
    current_user: UserModel, update_data: UpdateUserDTO, session: AsyncSession
):
    changes = update_data.model_dump(exclude_unset=True)

    if "avatar" in changes and changes["avatar"] is not None:
        changes["avatar"] = str(changes["avatar"])

    for field, value in changes.items():
        setattr(current_user, field, value)

    await session.commit()
    await session.refresh(current_user)

    return current_user


async def update_profile_avatar(
    update_avatar: UpdateAvatarDTO, current_user: UserModel, session: AsyncSession
):
    updated_avatar = update_avatar.model_dump(exclude_unset=True)

    current_user.avatar = updated_avatar["avatar"]

    await session.commit()
    await session.refresh(current_user)

    return updated_avatar
