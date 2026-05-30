from typing import Annotated
from annotated_types import Ge
from pydantic import BaseModel, ConfigDict
import uuid


Sets = Annotated[int, Ge(1)]
Reps = Annotated[int, Ge(1)]
Position = Annotated[int, Ge(1)]


class ProgramDayExerciseCreateInSchema(BaseModel):
    exercise_id: uuid.UUID
    sets: Sets | None = None
    reps: Reps | None = None
    position: Position | None = None


class ProgramDayExerciseUpdateInSchema(BaseModel):
    sets: Sets | None = None
    reps: Reps | None = None
    position: Position | None = None


class ProgramDayExerciseResponseOutSchema(BaseModel):
    id: uuid.UUID
    exercise_id: uuid.UUID
    program_day_id: uuid.UUID
    sets: Sets | None
    reps: Reps | None
    position: Position

    model_config = ConfigDict(from_attributes=True)