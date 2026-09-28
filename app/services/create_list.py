from app.schemas import Note, NoteCreate


def create_note(payload: NoteCreate) -> Note:
    raise NotImplementedError


def list_notes(tag: str | None = None) -> list[Note]:
    raise NotImplementedError
