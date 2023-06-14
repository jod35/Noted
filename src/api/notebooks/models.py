from sqlalchemy.orm import (
    DeclarativeBase,
    relationship,
    Mapped,
    mapped_column
)

from ..auth.models import User

class Base(DeclarativeBase):
    pass

class NoteBook(Base):
    __tablename__ = 'notebooks'
    id:Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)
    owner: Mapped[User] =relationship(back_populates="notebooks")    
    def __repr__(self) -> str:
        return f"<NoteBook {self.name}>"