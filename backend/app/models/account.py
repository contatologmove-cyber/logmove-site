from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from app.database import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(120))

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        index=True
    )

    phone: Mapped[str] = mapped_column(String(20))

    password_hash: Mapped[str] = mapped_column(String(255))

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )