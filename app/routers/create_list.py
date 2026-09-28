from fastapi import APIRouter, HTTPException

from app.schemas import Note, NoteCreate

create_list_router = APIRouter()


@create_list_router.post("/notes", status_code=201)
def create_note(payload: NoteCreate) -> Note:
    raise HTTPException(
        status_code=501, detail="Notizen anlegen und auflisten (#3) implementiert diesen Endpunkt"
    )


@create_list_router.get("/notes")
def list_notes(tag: str | None = None) -> list[Note]:
    raise HTTPException(
        status_code=501, detail="Notizen anlegen und auflisten (#3) implementiert diesen Endpunkt"
    )
