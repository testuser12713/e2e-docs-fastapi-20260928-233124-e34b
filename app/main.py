from fastapi import FastAPI

from app.config import Settings
from app.routers.create_list import create_list_router
from app.routers.notes_item import notes_item_router


def create_app() -> FastAPI:
    app = FastAPI(title="Notizen-API")

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "app_name": Settings().app_name}

    app.include_router(create_list_router)
    app.include_router(notes_item_router)
    return app


app = create_app()
