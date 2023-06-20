from sqlalchemy.orm import (
    relationship,
    Mapped,
    mapped_column
)
from datetime import datetime
from sqlalchemy import ForeignKey
from ..auth.models import User
from ..db.base import Base

class Note(Base):
    __tablename__ = 'notes'
    id: Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] =mapped_column(nullable=True)
    content:Mapped[str] = mapped_column(nullable=False)
    created:Mapped[datetime] = mapped_column(default=datetime.utcnow)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    notebook_id:Mapped[int] = mapped_column(ForeignKey('notebooks.id'))
    author:Mapped[User] = relationship(back_populates="notes")

    def __repr__(self) -> str:
        return f"<Note {self.title}>"