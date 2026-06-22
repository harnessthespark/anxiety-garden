"""
config.py — where settings come from.

LESSON: a backend should never hard-code secrets (like a database password) in
the code. Instead it reads them from the *environment* at run time. Locally that's
a .env file; on Coolify it's the env vars you set in the dashboard. Same code,
different settings, depending on where it runs.

`pydantic-settings` turns environment variables into a tidy, validated Python
object — it will complain loudly if something required is missing or the wrong type.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Read a local .env file if present; ignore any env vars we don't define here.
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # The database to connect to.
    # Default = a local SQLite file, so the app runs with ZERO setup while you learn.
    # In production you'll OVERRIDE this with a Postgres URL (set in Coolify).
    database_url: str = "sqlite:///./garden.db"


# One shared settings object the rest of the app imports.
settings = Settings()
