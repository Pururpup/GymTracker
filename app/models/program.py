import uuid
from sqlalchemy import String, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class Program(Base):
    __tablename__ = "programs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, autoincrement=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    program_name: Mapped[str] = mapped_column(String(255), nullable=False)
