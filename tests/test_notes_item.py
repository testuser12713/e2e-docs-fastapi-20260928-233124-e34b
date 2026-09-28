from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.main import create_app
from app.schemas import Note
from app.service import note_store


@pytest.fixture(autouse=True)
def reset_store():
    note_store._notes.clear()
    note_store._next_id = 1
    yield
    note_store._notes.clear()
    note_store._next_id = 1


def make_note(note_id: int) -> Note:
    return Note(
        id=note_id,
        titel=f"Notiz {note_id}",
        inhalt="Inhalt",
        tags=["tag"],
        erstellt_am=datetime(2026, 1, 1, 12, 0, 0),
    )


def test_get_known_id_returns_note():
    note_store._notes[1] = make_note(1)
    client = TestClient(create_app())
    response = client.get("/notes/1")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["titel"] == "Notiz 1"


def test_get_unknown_id_returns_404():
    client = TestClient(create_app())
    response = client.get("/notes/999")
    assert response.status_code == 404


def test_delete_removes_note_and_followup_get_returns_404():
    note_store._notes[1] = make_note(1)
    client = TestClient(create_app())
    response = client.delete("/notes/1")
    assert response.status_code == 204
    assert client.get("/notes/1").status_code == 404


def test_delete_unknown_id_returns_404():
    client = TestClient(create_app())
    response = client.delete("/notes/999")
    assert response.status_code == 404
