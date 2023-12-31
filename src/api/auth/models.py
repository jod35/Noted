from sqlalchemy.orm import (
    relationship,
    Mapped,
    mapped_column
)
from sqlalchemy_utils import EmailType
from sqlalchemy import Text
from typing import List
from ..db.base import Base




class User(Base):
    __tablename__ = 'users'
    id:Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(nullable=True)
    email:Mapped[str]=mapped_column(EmailType,nullable=False)
    password:Mapped[str]=mapped_column(Text,nullable=False)
    notes:Mapped[List["Note"]] = relationship(back_populates="author")
    notebooks:Mapped[List["NoteBook"]] = relationship(back_populates="owner")

    def __repr__(self) -> str:
        return f"<User {self.username}>"