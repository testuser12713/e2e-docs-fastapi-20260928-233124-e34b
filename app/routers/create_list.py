from fastapi import APIRouter

from app.schemas import Note, NoteCreate
from app.services.create_list import create_note, list_notes

create_list_router = APIRouter()


@create_list_router.post("/notes", status_code=201)
def post_note(payload: NoteCreate) -> Note:
    return create_note(payload)


@create_list_router.get("/notes")
def get_notes(tag: str | None = None) -> list[Note]:
    return list_notes(tag)
