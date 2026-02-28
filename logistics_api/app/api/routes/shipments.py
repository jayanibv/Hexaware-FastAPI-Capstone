from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user, require_role
from app.services.shipment_service import ShipmentService
from app.schemas.shipment_schema import ShipmentCreate, ShipmentStatusUpdate, ShipmentResponse

router = APIRouter(prefix="/shipments", tags=["Shipments"])


@router.post("", response_model=ShipmentResponse)
def create_shipment(
    data: ShipmentCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(["customer"]))
):
    return ShipmentService().create_shipment(db, user, data)


@router.get("/{tracking_number}", response_model=ShipmentResponse)
def get_shipment(
    tracking_number: str,
    db: Session = Depends(get_db),
    user=Depends(require_role(["customer", "agent"]))
):
    return ShipmentService().get_shipment(db, tracking_number, user)


@router.put("/{tracking_number}/status", response_model=ShipmentResponse)
def update_status(
    tracking_number: str,
    data: ShipmentStatusUpdate,
    db: Session = Depends(get_db),
    user=Depends(require_role(["agent"]))
):
    return ShipmentService().update_status(
        db, tracking_number, data.status, user
    )


@router.put("/{tracking_number}/cancel", response_model=ShipmentResponse)
def cancel_shipment(
    tracking_number: str,
    db: Session = Depends(get_db),
    user=Depends(require_role(["customer"]))
):
    return ShipmentService().cancel_shipment(db, tracking_number, user)