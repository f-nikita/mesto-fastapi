from fastapi import HTTPException

from app.constants import USER_IS_NOT_DEFINED
from app.data.users import fake_users_db
from app.schemas.user import UpdateAvatarDTO, UpdateUserDTO


def get_all_users():
    return list(fake_users_db.values())


def get_profile():
    user = fake_users_db.get("1")

    if user is None:
        raise HTTPException(status_code=404, detail=USER_IS_NOT_DEFINED)

    return user


def get_profile_by_id(user_id: str):
    user = fake_users_db.get(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail=USER_IS_NOT_DEFINED)

    return user


def update_profile(update_data: UpdateUserDTO):
    current_user = fake_users_db.get("1")

    if current_user is None:
        raise HTTPException(status_code=404, detail=USER_IS_NOT_DEFINED)

    updated_user = current_user.model_copy(
        update=update_data.model_dump(exclude_unset=True)
    )

    fake_users_db["1"] = updated_user

    return updated_user


def update_profile_avatar(update_data: UpdateAvatarDTO):
    current_user = fake_users_db.get("1")

    if current_user is None:
        raise HTTPException(status_code=404, detail=USER_IS_NOT_DEFINED)

    updated_user = current_user.model_copy(update={"avatar": update_data.avatar})

    fake_users_db["1"] = updated_user

    return updated_user
