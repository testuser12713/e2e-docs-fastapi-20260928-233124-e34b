from fastapi import APIRouter, HTTPException

from app.schemas import Note
from app.services.notes_item import delete_note, get_note

notes_item_router = APIRouter()


@notes_item_router.get("/notes/{note_id}")
def get_note_endpoint(note_id: int) -> Note:
    note = get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    return note


@notes_item_router.delete("/notes/{note_id}", status_code=204)
def delete_note_endpoint(note_id: int) -> None:
    if not delete_note(note_id):
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
