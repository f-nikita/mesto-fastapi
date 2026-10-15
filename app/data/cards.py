from app.schemas.card import Card

fake_cards_db: dict[str, Card] = {
    "1": Card(
        id="1",
        name="Nikitos",
        link=None,
        owner="Frontend developer",
        likes=False,
        createdAt="Frontend developer",
    ),
    "2": Card(
        id="2",
        name="Место",
        link="https://example.com/image.jpg",
        owner="1",
        likes=None,
        createdAt="2026-10-15",
    ),
}
