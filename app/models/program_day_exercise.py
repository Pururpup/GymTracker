import uuid
from sqlalchemy import String, UUID, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class ProgramDayExercise(Base):
    __tablename__ = "program_day_exercises"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, autoincrement=True, default=uuid.uuid4)
    exercise_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("exercises.id"), nullable=False)
    program_day_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("program_days.id"), nullable=False)
    sets: Mapped[int] = mapped_column(Integer, nullable=True)
    reps: Mapped[int] = mapped_column(Integer, nullable=True)
    position: Mapped[int] = mapped_column(Integer, nullable=False)

