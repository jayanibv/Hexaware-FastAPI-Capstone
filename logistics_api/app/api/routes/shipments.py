from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.core.database import SessionLocal
from app.services.shipment_service import ShipmentService
from app.core.dependencies import get_current_user
from app.schemas.shipment_schema import ShipmentCreate
from app.schemas.shipment_schema import ShipmentResponse
from app.models.shipment import Shipment

router = APIRouter(prefix="/shipments", tags=["Shipments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{shipment_id}")
def get_shipment(
    shipment_id: int,
    db: Session = Depends(get_db)
):
    shipment = ShipmentService().get_shipment_by_id(db, shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment

@router.post("", response_model=ShipmentResponse)
def create_shipment(
    data: ShipmentCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return ShipmentService().create_shipment(db, user, data)