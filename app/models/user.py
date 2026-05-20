import uuid
from sqlalchemy import String, BigInteger, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, autoincrement=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String(255), nullable=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
