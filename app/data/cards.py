from app.schemas.card import CardDTO

fake_cards_db: dict[str, CardDTO] = {
    "1": CardDTO(
        id="1",
        name="Nikitos",
        link=None,
        owner="Frontend developer",
        likes=False,
        createdAt="Frontend developer",
    ),
    "2": CardDTO(
        id="2",
        name="Место",
        link="https://example.com/image.jpg",
        owner="1",
        likes=None,
        createdAt="2026-10-15",
    ),
}
