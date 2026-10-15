from app.schemas.card import CardDTO

fake_cards_db: dict[str, CardDTO] = {
    "1": CardDTO(
        id="1",
        name="Nikitos",
        link="https://example.com/image.jpg",
        owner="Frontend developer",
        likes=False,
        created_at="Frontend developer",
    ),
    "2": CardDTO(
        id="2",
        name="Место",
        link="https://example.com/image.jpg",
        owner="1",
        likes=None,
        created_at="2026-10-15",
    ),
}
