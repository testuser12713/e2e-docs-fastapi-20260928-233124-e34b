from fastapi import APIRouter, HTTPException

from app.schemas import Note
from app.service import note_store

notes_router = APIRouter()


@notes_router.get("/notes/{note_id:int}")
def get_note(note_id: int) -> Note:
    note = note_store.find(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    return note


@notes_router.delete("/notes/{note_id:int}", status_code=204)
def delete_note(note_id: int) -> None:
    if not note_store.remove(note_id):
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
