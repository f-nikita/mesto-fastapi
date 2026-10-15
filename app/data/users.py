from app.schemas.user import User


fake_users_db: dict[str, User] = {
    "1": User(
        id="1",
        name="Никита",
        about="Python developer",
        avatar=None,
    ),
    "2": User(
        id="2",
        name="Анна",
        about="Frontend developer",
        avatar=None,
    ),
}
