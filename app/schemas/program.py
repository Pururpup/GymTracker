from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, ConfigDict
import uuid


ProgramName = Annotated[str, MinLen(1), MaxLen(255)]


class ProgramCreateInSchema(BaseModel):
    program_name: ProgramName


class ProgramUpdateInSchema(BaseModel):
    program_name: ProgramName


class ProgramResponseOutSchema(BaseModel):
    id: uuid.UUID
    program_name: ProgramName
    user_id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)
