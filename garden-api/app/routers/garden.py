"""
routers/garden.py — saving the garden state (blooms, weeds, bucket, wall…).

This one is a STUB on purpose — it's one of your later exercises (Lesson 6). For now
it just returns a placeholder so the app runs and you can see the route in /docs.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/garden", tags=["garden"])


@router.get("")
def get_garden():
    # 🏋️ YOUR TURN (Lesson 6): once there's a GardenState model + login, return the
    # logged-in person's saved garden from the database instead of this placeholder.
    return {"todo": "the garden state (blooms, weeds, bucket, wall) will live here"}
