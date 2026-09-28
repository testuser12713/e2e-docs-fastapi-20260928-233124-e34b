from app.schemas import Note


class NoteStore:
    def __init__(self) -> None:
        self._notes: dict[int, Note] = {}
        self._next_id: int = 1

    def find(self, note_id: int) -> Note | None:
        return self._notes.get(note_id)

    def remove(self, note_id: int) -> bool:
        if note_id not in self._notes:
            return False
        del self._notes[note_id]
        return True


note_store = NoteStore()
