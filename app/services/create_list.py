from datetime import UTC, datetime

from app.schemas import Note, NoteCreate
from app.store import note_store


def create_note(payload: NoteCreate) -> Note:
    note = Note(
        id=note_store._next_id,
        titel=payload.titel,
        inhalt=payload.inhalt,
        tags=payload.tags,
        erstellt_am=datetime.now(UTC),
    )
    note_store._notes[note.id] = note
    note_store._next_id += 1
    return note


def list_notes(tag: str | None = None) -> list[Note]:
    if tag is None:
        return list(note_store._notes.values())
    return [note for note in note_store._notes.values() if tag in note.tags]
