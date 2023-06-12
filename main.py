import asyncio 
from src.db.create_db import create_db
import uvicorn
from fastapi import FastAPI
from src.server.notes.routes import notes_router
from src.server.auth.routes import auth_router

app = FastAPI(
    description="A REST API for a note taking app"
)

app.include_router(notes_router,prefix="/notes")
app.include_router(auth_router,prefix="/auth")


