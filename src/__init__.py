from fastapi import FastAPI
from src.server.notes.routes import notes_router
from src.server.auth.routes import auth_router
from src.server.notebooks.routes import notebook_router

app = FastAPI(
    description="A REST API for a note taking app",
    docs_url="/"
)

app.include_router(notes_router,prefix="/notes")
app.include_router(auth_router,prefix="/auth")
app.include_router(notebook_router,prefix="/notebooks")