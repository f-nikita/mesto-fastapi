from fastapi import HTTPException

from app.constants import CARD_IS_NOT_DEFINED
from app.data.cards import fake_cards_db
from app.schemas.card import Card


def get_all_cards():
    return list(fake_cards_db.values())


def get_card_by_id(card_id: str):
    card = fake_cards_db.get(card_id)

    if card is None:
        raise HTTPException(status_code=404, detail=CARD_IS_NOT_DEFINED)

    return card


def create_card(item: Card):
    new_id = str(len(fake_cards_db) + 1)
    new_card = item.model_copy(update={"id": new_id})
    fake_cards_db[new_id] = new_card
    return new_card


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
