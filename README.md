# Notizen-API

Kleine REST-API in Python, die Notizen (id, titel, inhalt, tags, erstellt_am) ohne
Datenbank in einem In-Memory-Speicher verwaltet. Sie ist als Sprint-Skelett angelegt:
der Health-Endpunkt ist funktionsfähig, die vier Notiz-Endpunkte sind registriert und
werden in nachfolgenden Tickets implementiert (antworten aktuell mit 501).

## Tech-Stack

- **Sprache**: Python
- **Framework**: FastAPI
- **Validierung**: Pydantic v2 (`model_config`, `field_validator`)
- **Konfiguration**: pydantic-settings
- **Speicher**: In-Memory (keine Datenbank)
- **Testing**: pytest + FastAPI-TestClient
- **Runtime**: uvicorn

## Installation

```bash
pip install -r requirements.txt
```

## Start (Dev)

```bash
uvicorn app.main:app --reload
```

Alternativ ohne Reload:

```bash
uvicorn app.main:app
```

## Konfiguration

Die App liest ihre Einstellungen aus der Umgebung (und optional aus einer `.env`-Datei).

| Variable   | Default      | Beschreibung                          |
| ---------- | ------------ | ------------------------------------- |
| `APP_NAME` | `Notizen-API` | Name der Anwendung (erscheint in `/health`) |

## Endpunkte

| Methode | Pfad                | Beschreibung                                  | Antwort                                   |
| ------- | ------------------- | --------------------------------------------- | ----------------------------------------- |
| GET     | `/health`           | Health-Check                                  | `200 {"status":"ok","app_name":"..."}`    |
| POST    | `/notes`            | Notiz anlegen (Body: `NoteCreate`)            | `201 Note` / `422` bei Validierungsfehler |
| GET     | `/notes`            | Alle Notizen auflisten (optional `?tag=...`)  | `200 list[Note]`                          |
| GET     | `/notes/{note_id}`  | Einzelne Notiz abrufen                        | `200 Note` / `404`                        |
| DELETE  | `/notes/{note_id}`  | Notiz löschen                                 | `204` / `404`                             |

### Datenformen

`NoteCreate`:

```json
{ "titel": "Einkaufen", "inhalt": "Milch und Brot", "tags": ["privat", "einkauf"] }
```

- `titel`: 1–100 Zeichen
- `tags`: maximal 5 Einträge

`Note`:

```json
{
  "id": 1,
  "titel": "Einkaufen",
  "inhalt": "Milch und Brot",
  "tags": ["privat", "einkauf"],
  "erstellt_am": "2026-09-28T12:00:00Z"
}
```

## Tests

```bash
pytest
```

## Features

- Health-Endpoint mit konfigurierbarem App-Namen
- Pydantic-v2-Modelle für Notizen (Validierung von Titel und Tags)
- Gemeinsamer In-Memory-Speicher (`NoteStore`) für beide Feature-Tickets
- Notiz-Routen (POST/GET `/notes`, GET/DELETE `/notes/{note_id}`) als registrierte Stubs
