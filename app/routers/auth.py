from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.auth import LoginDTO, TokenDTO
from app.schemas.user import CreateUserDTO, UserDTO
from app.services.auth import login_user, register_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/signup",
    response_model=UserDTO,
    status_code=status.HTTP_201_CREATED,
    responses={409: {"description": "Email уже используется"}},
)
async def signup(
    user_data: CreateUserDTO,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    return await register_user(user_data, session)


@router.post("/signin", response_model=TokenDTO)
async def signin(
    login_data: LoginDTO,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    access_token = await login_user(login_data, session)

    return TokenDTO(access_token=access_token)
