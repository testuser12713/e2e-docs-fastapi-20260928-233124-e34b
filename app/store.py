from app.schemas import Note


class NoteStore:
    def __init__(self) -> None:
        self._notes: dict[int, Note] = {}
        self._next_id: int = 1


note_store = NoteStore()
