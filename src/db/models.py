from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy_utils import EmailType
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Integer,String,ForeignKey,Text
from datetime import datetime
from typing import List



class Base(DeclarativeBase):
    pass


class NoteBook(Base):
    __tablename__ = 'notebooks'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    notes:Mapped[List['Note']] = relationship('Note',back_populates='notes')
    user_id:Mapped[int] = ForeignKey('user.id')
    creator:Mapped["User"] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"<Book {self.name}>"


class Note(Base):
    __tablename__ = 'notes'
    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column(nullable=False)
    content : Mapped[str] = mapped_column(Text,nullable=False)
    created : Mapped[datetime] =mapped_column(default=datetime.utcnow)
    book_id  :Mapped[int] = ForeignKey('notebooks.id')
    user_id : Mapped[int]=ForeignKey('user.id')
    author : Mapped["User"] = relationship(back_populates="user")



    def __repr__(self) -> str:
        return f"<Note {self.title}>"
    

class User(Base):
    __tablename__ = 'users'
    id : Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column(nullable=False)
    email : Mapped[str] = mapped_column(EmailType,nullable=False)
    password_hash : Mapped[str] = mapped_column(Text,nullable=False)
    notes : Mapped[List["Note"]] = relationship(back_populates="notes")
    notebooks : Mapped[List["NoteBook"]] = relationship(back_populates="notebooks")

    def __repr__(self) -> str:
        return f"<User {self.email}>"