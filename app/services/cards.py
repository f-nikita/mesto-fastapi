from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.constants import CARD_IS_NOT_DEFINED
from app.data.cards import fake_cards_db
from app.models.card import CardModel
from app.models.user import UserModel
from app.schemas.card import CardDTO


async def get_all_cards(session: AsyncSession) -> list[CardModel]:
    result = await session.execute(select(CardModel))
    return list(result.scalars().all())


async def get_card_by_id(card_id: UUID, session: AsyncSession):
    card = await session.get(CardModel, card_id)

    if card is None:
        raise HTTPException(status_code=401, detail=CARD_IS_NOT_DEFINED)

    return card


async def create_card(
    item: CardDTO,
    current_user: UserModel,
    session: AsyncSession,
) -> CardModel:

    card = CardModel(
        name=item.name,
        link=item.link,
        owner_id=current_user,
    )

    session.add(card)
    await session.commit()
    await session.refresh(card)

    return card


def delete_card(card_id: str):
    card = fake_cards_db.get(card_id)

    if card is None:
        raise HTTPException(status_code=404, detail=CARD_IS_NOT_DEFINED)

    del fake_cards_db[card_id]
    return card


def add_like(card_id: str):
    current_card = fake_cards_db.get(card_id)

    if current_card is None:
        raise HTTPException(status_code=404, detail=CARD_IS_NOT_DEFINED)

    updated_card = current_card.model_copy(update={"likes": True})

    fake_cards_db[card_id] = updated_card

    return updated_card


def delete_like(card_id: str):
    current_card = fake_cards_db.get(card_id)

    if current_card is None:
        raise HTTPException(status_code=404, detail=CARD_IS_NOT_DEFINED)

    updated_card = current_card.model_copy(update={"likes": False})

    fake_cards_db[card_id] = updated_card

    return updated_card
