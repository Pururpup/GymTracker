from typing import Annotated
from annotated_types import MinLen, MaxLen, Ge
from pydantic import BaseModel, ConfigDict
import uuid


Username = Annotated[str, MinLen(1), MaxLen(255)]
TelegramId = Annotated[int, Ge(1)]


class UserCreateInSchema(BaseModel):
    telegram_id: TelegramId
    username: Username | None = None # поле можно вообще не передавать, в таком случае будет None


class UserResponseOutSchema(BaseModel):
    id: uuid.UUID
    username: Username | None # поле должно быть передано, но может быть None
    telegram_id: TelegramId

    model_config = ConfigDict(from_attributes=True)
