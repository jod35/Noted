from fastapi import FastAPI
from .api.auth.routes import auth_router
from .api.notebooks.routes import noteb_router
from .api.notes.routes import note_router


app = FastAPI(
    title="Noter",
    description="A REST API for a note taking application",
    docs_url="/"
) 


app.include_router(auth_router,prefix="/auth")
app.include_router(noteb_router,prefix="/notebooks")
app.include_router(note_router,prefix="/notes")