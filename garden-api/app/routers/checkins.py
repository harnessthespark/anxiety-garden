from datetime import datetime, timezone
from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..database import get_session
from ..models import CheckIn


# prefix → every URL here starts with /checkins. tags → groups them in /docs.
router = APIRouter(prefix="/checkins", tags=["check-ins"])


@router.post("")
def log_checkin(checkin: CheckIn, session: Session = Depends(get_session)):
    """Save one reading.

    Read the two arguments — they're the heart of FastAPI:
      • `checkin: CheckIn`        → FastAPI reads the JSON body and validates it
                                    against the model. Bad data is rejected for you.
      • `Depends(get_session)`    → "dependency injection": FastAPI calls get_session()
                                    and hands you a ready database session.
    """
    session.add(checkin)       # 1. stage the new row
    session.commit()           # 2. write it to the database
    session.refresh(checkin)   # 3. reload it so we get the generated id/timestamp back
    return checkin             # returned as JSON automatically

@router.get("")
def list_checkins(session: Session = Depends(get_session)):
      """All readings, oldest first."""
      return session.exec(select(CheckIn).order_by(CheckIn.created_at)).all()

@router.get("/today")
def todays_checkins(session: Session = Depends(get_session)):
    # midnight this morning, in UTC
    start = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    # ask the DB for only the rows created at or after that moment
    return session.exec(
        select(CheckIn).where(CheckIn.created_at >= start)
    ).all()