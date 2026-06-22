"""
database.py — the connection to the database.

Two ideas to hold onto:
  1. The ENGINE — one long-lived object that knows how to talk to the database.
     Think of it as the phone *line*.
  2. A SESSION — a short-lived "conversation" you open for one request and close
     when you're done. Think of it as a phone *call* on that line.
"""
from sqlmodel import create_engine, Session, SQLModel

from .config import settings

# SQLite is fussy about being used across threads; this arg relaxes that.
# It's only needed for SQLite, and harmless otherwise.
connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}

# echo=True prints every SQL statement to your terminal. Brilliant for *seeing*
# what the ORM is doing under the hood while you learn. Turn it off in production.
engine = create_engine(settings.database_url, echo=True, connect_args=connect_args)


def create_db_and_tables() -> None:
    """Create the tables from your models if they don't exist yet.
    Fine while learning. Later you'll replace this with Alembic *migrations* —
    a safer way to evolve the schema once there's real data you can't just delete."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """FastAPI calls this for each request: it hands your endpoint a session,
    then closes it automatically afterwards (that's what `with ... yield` gives us)."""
    with Session(engine) as session:
        yield session
