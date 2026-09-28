from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_validator


class NoteCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    titel: str
    inhalt: str
    tags: list[str]

    @field_validator("titel")
    @classmethod
    def validate_titel(cls, v: str) -> str:
        if not 1 <= len(v) <= 100:
            raise ValueError("titel muss zwischen 1 und 100 Zeichen lang sein")
        return v

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, v: list[str]) -> list[str]:
        if len(v) > 5:
            raise ValueError("maximal 5 Tags erlaubt")
        return v


class Note(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    titel: str
    inhalt: str
    tags: list[str]
    erstellt_am: datetime
