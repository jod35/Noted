from sqlalchemy.orm import (
    relationship,
    Mapped,
    mapped_column
)

from ..auth.models import User
from ..db.base import Base


class NoteBook(Base):
    __tablename__ = 'notebooks'
    id:Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)
    owner: Mapped[User] =relationship(back_populates="notebooks")    
    def __repr__(self) -> str:
        return f"<NoteBook {self.name}>"