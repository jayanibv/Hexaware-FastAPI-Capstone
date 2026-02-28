from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.tracking_schema import TrackingCreate, TrackingResponse
from app.services.tracking_service import TrackingService
from app.dependencies import require_role, get_current_user

router = APIRouter(prefix="/tracking", tags=["Tracking"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=TrackingResponse)
def add_tracking(
    data: TrackingCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(require_role(["ADMIN", "AGENT"]))
):
    return TrackingService().add_tracking(db, data)


@router.get("/{tracking_number}", response_model=list[TrackingResponse])
def get_tracking_history(
    tracking_number: str,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return TrackingService().get_tracking_history(db, tracking_number)