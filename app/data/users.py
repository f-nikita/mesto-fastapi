from app.schemas.user import UserDTO

fake_users_db: dict[str, UserDTO] = {
    "1": UserDTO(
        id="1",
        name="Никита",
        about="Python developer",
        avatar=None,
    ),
    "2": UserDTO(
        id="2",
        name="Анна",
        about="Frontend developer",
        avatar=None,
    ),
}
