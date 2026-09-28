from fastapi.testclient import TestClient

from app.main import app
from app.store import note_store


def _reset_store() -> None:
    note_store._notes.clear()
    note_store._next_id = 1


def test_post_note_returns_id_and_erstellt_am() -> None:
    _reset_store()
    with TestClient(app) as client:
        response = client.post(
            "/notes",
            json={"titel": "Erste Notiz", "inhalt": "Hallo", "tags": ["a"]},
        )
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["titel"] == "Erste Notiz"
    assert "erstellt_am" in body


def test_post_note_empty_titel_422() -> None:
    _reset_store()
    with TestClient(app) as client:
        response = client.post("/notes", json={"titel": "", "inhalt": "x", "tags": []})
    assert response.status_code == 422


def test_post_note_titel_too_long_422() -> None:
    _reset_store()
    with TestClient(app) as client:
        response = client.post("/notes", json={"titel": "x" * 101, "inhalt": "x", "tags": []})
    assert response.status_code == 422


def test_post_note_too_many_tags_422() -> None:
    _reset_store()
    with TestClient(app) as client:
        response = client.post(
            "/notes",
            json={"titel": "T", "inhalt": "x", "tags": ["a", "b", "c", "d", "e", "f"]},
        )
    assert response.status_code == 422


def test_get_notes_returns_all_created() -> None:
    _reset_store()
    with TestClient(app) as client:
        client.post("/notes", json={"titel": "A", "inhalt": "", "tags": ["x"]})
        client.post("/notes", json={"titel": "B", "inhalt": "", "tags": ["y"]})
        response = client.get("/notes")
    assert response.status_code == 200
    body = response.json()
    assert len(body) == 2
    assert {n["titel"] for n in body} == {"A", "B"}


def test_get_notes_filter_by_tag() -> None:
    _reset_store()
    with TestClient(app) as client:
        client.post("/notes", json={"titel": "A", "inhalt": "", "tags": ["xyz"]})
        client.post("/notes", json={"titel": "B", "inhalt": "", "tags": ["other"]})
        response = client.get("/notes", params={"tag": "xyz"})
    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["titel"] == "A"
