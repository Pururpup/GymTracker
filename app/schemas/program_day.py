from typing import Annotated
from annotated_types import MinLen, MaxLen, Ge
from pydantic import BaseModel, ConfigDict
import uuid


NameOfDay = Annotated[str, MinLen(1), MaxLen(255)]
Position = Annotated[int, Ge(1)]


class ProgramDayCreateInSchema(BaseModel):
    name_of_day: NameOfDay
    position: Position | None = None # если None, то бэкенд сам поставит max + 1


class ProgramDayUpdateInSchema(BaseModel):
    name_of_day: NameOfDay
    position: Position | None = None


class ProgramDayResponseOutSchema(BaseModel):
    id: uuid.UUID
    name_of_day: NameOfDay
    program_id: uuid.UUID
    position: Position

    model_config = ConfigDict(from_attributes=True)
