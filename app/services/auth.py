from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import UserModel
from app.schemas.auth import LoginDTO
from app.schemas.user import CreateUserDTO
from app.security import create_access_token, hash_password, verify_password


async def register_user(
    user_data: CreateUserDTO,
    session: AsyncSession,
) -> UserModel:
    existing_user = await session.scalar(
        select(UserModel).where(UserModel.email == user_data.email),
    )

    if existing_user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким email уже существует",
        )

    user = UserModel(
        name=user_data.name,
        about=user_data.about,
        avatar=str(user_data.avatar) if user_data.avatar else None,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user


async def login_user(
    login_data: LoginDTO,
    session: AsyncSession,
) -> str:
    user = await session.scalar(
        select(UserModel).where(UserModel.email == login_data.email),
    )

    if user is None or not verify_password(
        login_data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный email или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return create_access_token(user.id)
