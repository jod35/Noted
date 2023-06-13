from fastapi import APIRouter
from ...utils.db_notes import get_all_notes
from ...db.base import async_session
from ...schemas.notes import NoteCreationSchema

from typing import List

notes_router = APIRouter(tags=["notes"])

@notes_router.get('/',response_model=List[NoteCreationSchema])
async def get_all_notes():
    pass
    