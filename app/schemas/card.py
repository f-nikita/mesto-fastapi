from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field, HttpUrl


class CreateCardDTO(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    link: HttpUrl


class CardDTO(CreateCardDTO):
    id: UUID
    owner: UUID
    likes: list[UUID] = Field(default_factory=list)
    created_at: datetime


# name: {
#     type: String,
#     required: true,
#     minlength: 2,
#     maxlength: 30,
#   },
#   link: {
#     type: String,
#     required: true,
#   },
#   owner: {
#     type: mongoose.Schema.Types.ObjectId,
#     required: true,
#   },
#   likes: {
#     type: [mongoose.Schema.Types.ObjectId],
#     default: [],
#   },
#   createdAt: {
#     type: mongoose.Schema.Types.Date,
#     default: Date.now(),
