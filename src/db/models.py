from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
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

    def __repr__(self) -> str:
        return f"<Book {self.name}>"
    
    async def save(self,async_session:AsyncSession):
        await async_session.add(self)
        await async_session.commit()



class Note(Base):
    __tablename__ = 'notes'
    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(nullable=False)
    content:Mapped[str] =mapped_column(Text,nullable=False)
    created:Mapped[datetime] =mapped_column(default=datetime.utcnow)
    book_id:Mapped[int] = ForeignKey('notebooks.id')


    def __repr__(self) -> str:
        return f"<Note {self.title}>"