from app.schemas import Note
from app.store import note_store


def get_note(note_id: int) -> Note | None:
    return note_store._notes.get(note_id)


def delete_note(note_id: int) -> bool:
    if note_id not in note_store._notes:
        return False
    del note_store._notes[note_id]
    return True
