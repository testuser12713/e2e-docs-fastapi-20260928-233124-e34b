from fastapi import APIRouter, HTTPException

from app.schemas import Note

notes_item_router = APIRouter()


@notes_item_router.get("/notes/{note_id}")
def get_note(note_id: int) -> Note:
    raise HTTPException(
        status_code=501,
        detail="Einzelne Notiz abrufen und löschen (#1) implementiert diesen Endpunkt",
    )


@notes_item_router.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int) -> None:
    raise HTTPException(
        status_code=501,
        detail="Einzelne Notiz abrufen und löschen (#1) implementiert diesen Endpunkt",
    )
