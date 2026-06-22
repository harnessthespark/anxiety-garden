"""
main.py — the application itself. This is what `uvicorn` runs:

    uvicorn app.main:app --reload
                  ^^^^ ^
                  file └ the variable named `app` below
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import create_db_and_tables
from .routers import checkins, garden


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Everything before `yield` runs ONCE when the app starts up.
    create_db_and_tables()   # make sure the tables exist
    yield
    # Anything after `yield` would run on shutdown (we don't need anything yet).


app = FastAPI(title="The Garden API", lifespan=lifespan)

# CORS = "Cross-Origin Resource Sharing". Your frontend (garden.html) lives at a
# different web address than this API, and browsers block that by default for safety.
# This explicitly says "these origins are allowed to call me".
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8770",                  # your local garden.html preview
        "https://garden.harnessthespark.com",     # production frontend (later)
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach the routers — this is what makes /checkins and /garden exist.
app.include_router(checkins.router)
app.include_router(garden.router)


@app.get("/health")
def health():
    """A tiny endpoint Coolify can ping to check the app is alive."""
    return {"status": "ok"}
