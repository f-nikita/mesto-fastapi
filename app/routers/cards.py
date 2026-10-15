from fastapi import APIRouter

from app.constants import CARD_IS_NOT_DEFINED
from app.schemas.card import CardDTO
from app.services import cards as cards_services

router = APIRouter(prefix="/cards", tags=["cards"])


@router.get("", response_model=list[CardDTO])
async def get_all_cards():
    return cards_services.get_all_cards()


@router.get(
    "/{card_id}",
    response_model=CardDTO,
    responses={404: {"description": CARD_IS_NOT_DEFINED}},
)
async def get_card_by_id(card_id: str):
    return cards_services.get_card_by_id(card_id)


@router.post("", response_model=CardDTO, status_code=201)
async def create_card(item: CardDTO):
    return cards_services.create_card(item)


@router.delete(
    "/{card_id}",
    response_model=CardDTO,
    responses={404: {"description": CARD_IS_NOT_DEFINED}},
)
async def delete_card(card_id: str):
    return cards_services.delete_card(card_id)


@router.put(
    "/{card_id}/likes",
    response_model=CardDTO,
    responses={404: {"description": CARD_IS_NOT_DEFINED}},
)
async def add_like(card_id: str):
    return cards_services.add_like(card_id)


@router.delete(
    "/{card_id}/likes",
    response_model=CardDTO,
    responses={404: {"description": CARD_IS_NOT_DEFINED}},
)
async def delete_like(card_id: str):
    return cards_services.delete_like(card_id)
