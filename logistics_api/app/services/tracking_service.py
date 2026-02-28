from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.tracking import Tracking
from app.repositories.tracking_repository import TrackingRepository
from app.repositories.shipment_repository import ShipmentRepository


class TrackingService:

    def get_tracking_history(self, db: Session, tracking_number: str):
        shipment_repo = ShipmentRepository()
        tracking_repo = TrackingRepository()

        shipment = shipment_repo.get_by_tracking(db, tracking_number)

        if not shipment:
            raise HTTPException(status_code=404, detail="Shipment not found")

        return tracking_repo.get_by_shipment(db, shipment.id)


    def add_tracking_entry(self, db: Session, shipment_id, location: str, status: str):
        tracking_repo = TrackingRepository()

        tracking = Tracking(
            shipment_id=shipment_id,
            location=location,
            status=status
        )

    def add_tracking_update(self, db: Session, tracking_number: str, data, user):
        shipment_repo = ShipmentRepository()
        shipment = shipment_repo.get_by_tracking(db, tracking_number)

        if not shipment:
            raise HTTPException(status_code=404, detail="Shipment not found")

        return self.add_tracking_entry(
            db,
            shipment_id=shipment.id,
            location=data.location,
            status=data.status
        )