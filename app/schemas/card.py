from pydantic import BaseModel


class Card(BaseModel):
    id: str
    name: str
    link: str | None = None
    owner: str
    likes: bool | None = None
    createdAt: str


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
