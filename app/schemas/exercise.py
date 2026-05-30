from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, ConfigDict
import uuid


ExerciseName = Annotated[str, MinLen(1), MaxLen(255)]


class ExerciseCreateInSchema(BaseModel):
    exercise_name: ExerciseName


class ExerciseUpdateInSchema(BaseModel):
    exercise_name: ExerciseName


class ExerciseResponseOutSchema(BaseModel):
    id: uuid.UUID
    exercise_name: ExerciseName
    user_id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)
