from fastapi import FastAPI

from app.routers.cards import router as card_router
from app.routers.users import router as users_router

app = FastAPI()

app.include_router(users_router)
app.include_router(card_router)
