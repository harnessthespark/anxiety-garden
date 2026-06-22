# The Garden API — your FastAPI learning project

This is the backend for the Garden tracker: it stores **check-ins** (your "emotional
weather" readings) so patterns can surface over days and months. It's also your
**FastAPI training project** — every file is commented to teach, and there are
🏋️ **Your turn** exercises in the code.

**Stack:** FastAPI (web framework) · SQLModel (tables + validation) · SQLite locally →
PostgreSQL in production · deployed on Coolify/Hetzner.

---

## 1. Run it (≈5 minutes, no database to install)

```bash
cd ~/garden-api
python3 -m venv .venv          # a "virtual environment" = an isolated set of libraries for this project
source .venv/bin/activate      # turn it on — you'll see (.venv) appear in your prompt
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open **http://localhost:8000/docs** — FastAPI built you an interactive API explorer
for free. Try it:

1. Expand **POST /checkins** → *Try it out* → send `{ "weather": "stormy" }` → *Execute*.
2. Expand **GET /checkins** → *Execute* → you'll see the reading you just saved.

It saved to a local file `garden.db` (SQLite). That's a working backend. 🎉

> `--reload` restarts the server whenever you save a file — leave it running while you learn.
> Stop the server with **Ctrl-C**.

---

## 2. The map — read the files in this order

| Order | File | The concept it teaches |
|---|---|---|
| 1 | `app/config.py` | reading settings from the environment, not hard-coding them |
| 2 | `app/database.py` | engine vs session |
| 3 | `app/models.py` | an ORM: Python classes ⇄ database rows |
| 4 | `app/routers/checkins.py` | routing + dependency injection (`Depends`) |
| 5 | `app/main.py` | wiring routers together, startup, CORS |
| 6 | `Dockerfile` | what a container is |

Each file is short and commented. Read the comments — they're the lesson.

---

## 3. The big ideas, in plain English

- **The ORM (SQLModel).** Instead of writing SQL by hand, you write Python classes;
  the ORM turns them into tables and turns rows back into objects. `echo=True` in
  `database.py` prints the real SQL it generates — watch your terminal as you click
  around `/docs` and you'll *see* it.
- **Engine vs session.** The *engine* is the open phone line to the database. A
  *session* is one call — opened per request, closed after. `get_session()` does that.
- **Dependency injection.** `Depends(get_session)` is FastAPI handing your function the
  things it needs. You'll meet this pattern everywhere (later: `Depends(current_user)`).
- **Validation & docs for free.** Because an endpoint says `checkin: CheckIn`, FastAPI
  checks the incoming JSON, rejects bad data, *and* documents it in `/docs` — no extra work.

---

## 4. Your learning path (in order)

Each step is a small, real lesson. The 🏋️ markers in the code are the hands-on bits.

1. **Add a field.** In `models.py`, add `note: str | None = None` to `CheckIn`. Delete
   `garden.db`, restart, and watch the new field appear in `/docs`. *(How the schema and
   the API stay in sync.)*
2. **Write an endpoint.** Add `GET /checkins/today` in `checkins.py` (hint in the file).
   *(Routing + filtering a query.)*
3. **Switch to real Postgres.** `docker compose up -d` starts a local Postgres just like
   production. Copy the Postgres line from `.env.example` into a new `.env`, restart
   uvicorn. Same code, real database. *(The production setup.)*
4. **Add migrations (Alembic).** Once data's real you can't just delete the DB to change
   it — Alembic records each schema change as a versioned step. *(We'll do this together.)*
5. **Add auth.** Magic-link or JWT, then make `/checkins` return only the logged-in
   person's rows. *(The security lesson — the most important one.)*
6. **Build the garden router.** Flesh out `garden.py` to save blooms/weeds/bucket/wall.
7. **GDPR: export & delete.** Endpoints so someone can download or erase all their data.
   *(Because this is wellbeing data — we design it in, not bolt it on.)*

---

## 5. Deploy to Coolify (when you're ready)

1. Push this folder to a GitHub repo.
2. Coolify → add a **PostgreSQL** database resource → copy its connection string.
3. Coolify → new **Application** from the repo → set env var `DATABASE_URL` to that
   string → set the domain (`garden.harnessthespark.com`). Coolify builds the
   `Dockerfile`; Traefik adds HTTPS automatically.
4. Your `garden.html` frontend `fetch()`es `https://garden.harnessthespark.com`.

Same Hetzner box, same Coolify, same Postgres pattern as your other apps — only the
framework inside the container is different.

---

## ⚠️ One note on the data model

The `CheckIn` fields (`weather`, `emotion`, `trigger`, `context`) are **provisional** —
they mirror the "emotional weather" design we're still finalising. We'll lock that
*before* Lesson 4 (migrations), so the table doesn't need reshaping later.
