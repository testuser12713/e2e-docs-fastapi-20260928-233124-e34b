from app.schemas import Note


def get_note(note_id: int) -> Note | None:
    raise NotImplementedError


def delete_note(note_id: int) -> bool:
    raise NotImplementedError
