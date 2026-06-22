"""
models.py — the SHAPE of your data (your database tables).

Each class with `table=True` becomes one TABLE. Each attribute becomes one COLUMN.
SQLModel reads the Python type hints (uuid.UUID, str, datetime, `str | None`…) and
builds the table for you — and the SAME class validates incoming JSON. One source
of truth for both. That's the magic of an ORM.

NOTE: the CheckIn fields are PROVISIONAL — they mirror the "emotional weather" model
we're still finalising. We'll lock that before we add migrations, so the table
doesn't need reshaping later.
"""
from datetime import datetime, timezone
import uuid

from sqlmodel import SQLModel, Field


def now() -> datetime:
    """Current time, timezone-aware (UTC). Used as the default for timestamp columns."""
    return datetime.now(timezone.utc)


class User(SQLModel, table=True):
    # A UUID primary key is unguessable (better than 1, 2, 3… for anything public-facing).
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(index=True, unique=True)  # index → fast lookups; unique → no duplicates
    created_at: datetime = Field(default_factory=now)


class CheckIn(SQLModel, table=True):
    """One 'sundial reading' — how the weather was at a moment in time.
    These rows are what accumulate into months of pattern."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    # Optional for now (no auth yet). Becomes required once we add login — then every
    # check-in belongs to a person, and people only see their own.
    user_id: uuid.UUID | None = Field(default=None, foreign_key="user.id", index=True)
    created_at: datetime = Field(default_factory=now, index=True)

    weather: str                        # "stormy" | "sunny" | "overcast" | "foggy" | "clear"
    emotion: str | None = None          # the word(s) off the wheel / sundial
    trigger: str | None = None          # what tripped the alarm
    context: str | None = None          # what was happening at the time
    note: str    | None = None          # "rough morning, better by lunch."
