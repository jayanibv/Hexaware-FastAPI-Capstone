from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.shipment_schema import (
    ShipmentCreate,
    ShipmentResponse,
    UpdateStatusRequest
)
from app.services.shipment_service import ShipmentService
from app.dependencies import get_current_user, require_role

router = APIRouter(prefix="/shipments", tags=["Shipments"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=ShipmentResponse)
def create_shipment(
    data: ShipmentCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(require_role(["CUSTOMER"]))
):
    return ShipmentService().create_shipment(db, user_id, data)


@router.get("/{tracking_number}", response_model=ShipmentResponse)
def get_shipment(
    tracking_number: str,
    db: Session = Depends(get_db)
):
    return ShipmentService().get_shipment(db, tracking_number)


@router.put("/{tracking_number}/status", response_model=ShipmentResponse)
def update_status(
    tracking_number: str,
    data: UpdateStatusRequest,
    db: Session = Depends(get_db),
    user_id: int = Depends(require_role(["ADMIN", "AGENT"]))
):
    return ShipmentService().update_status(db, tracking_number, data.status)