from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, require_role
from app.services.tracking_service import TrackingService
from app.schemas.tracking_schema import TrackingCreate, TrackingResponse

router = APIRouter(prefix="/tracking", tags=["Tracking"])


@router.get("/{tracking_number}", response_model=list[TrackingResponse])
def tracking_history(
    tracking_number: str,
    db: Session = Depends(get_db),
    user=Depends(require_role(["customer", "agent"]))
):
    return TrackingService().get_tracking_history(db, tracking_number)


@router.post("/{tracking_number}", response_model=TrackingResponse)
def add_tracking_update(
    tracking_number: str,
    data: TrackingCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(["agent"]))
):
    return TrackingService().add_tracking_update(db, tracking_number, data, user)