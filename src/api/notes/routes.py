from fastapi import APIRouter


note_router = APIRouter(
    tags=["notes"]
)

@note_router.get("/")
async def get_all_notes() -> dict:
    """Retrieve all notes
    """
    pass

@note_router.get("/{note_id}")
async def get_note_by_id(note_id:int)->dict:
    """Retrieve note by ID
    ### Parameters
    - note_id: int
    """
    pass

@note_router.patch("/{note_id}")
async def update_note(note_id:int)->dict:
    """Update note by ID
    ### Parameters
    - note_id: int
    """
    pass

@note_router.put("/{note_id}")
async def partially_update_note(note_id:int)->dict:
    """Update note by ID
    ### Parameters
    - note_id: int
    """
    pass

@note_router.delete("/{note_id}")
async def delete_note(note_id:int)->dict:
    """Delete note by ID
    ### Parameters
    - note_id: int
    """
    pass

