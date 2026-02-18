
from app.db.session import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Date, Text
from datetime import date


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    category: Mapped[str] = mapped_column(String(50), default="general")
    difficulty: Mapped[int] = mapped_column(Integer, default=3)
    estimated_minutes: Mapped[int] = mapped_column(Integer, default=30)
    deadline: Mapped[date | None] = mapped_column(Date, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
