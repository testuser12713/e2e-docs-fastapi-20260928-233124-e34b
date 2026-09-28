from fastapi.testclient import TestClient

from app.main import create_app
from app.routers.create_list import create_list_router
from app.routers.notes import notes_router


def test_health_returns_status_ok_and_configured_app_name():
    client = TestClient(create_app())
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["app_name"] == "Notizen-API"


def test_all_four_note_routes_are_registered():
    app = create_app()
    client = TestClient(app)

    # Collection routes never answer 404 (200/201/422 once implemented), so a
    # "not a 404" check is safe on both sides of the stub gap.
    assert client.post("/notes", json={"titel": "T", "inhalt": "", "tags": []}).status_code != 404
    assert client.get("/notes").status_code != 404

    # Item routes answer 404 for unknown ids once implemented, so assert their
    # registration (path + verb) structurally instead of via a status code.
    registered = {
        (route.path, frozenset(route.methods))
        for router in (create_list_router, notes_router)
        for route in router.routes
    }
    assert ("/notes", frozenset({"POST"})) in registered
    assert ("/notes", frozenset({"GET"})) in registered
    assert ("/notes/{note_id:int}", frozenset({"GET"})) in registered
    assert ("/notes/{note_id:int}", frozenset({"DELETE"})) in registered
