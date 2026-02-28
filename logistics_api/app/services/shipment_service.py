import random
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.shipment import Shipment
from app.models.tracking import Tracking
from app.repositories.shipment_repository import ShipmentRepository
from app.repositories.tracking_repository import TrackingRepository


class ShipmentService:

    def create_shipment(self, db: Session, user, data):
        repo = ShipmentRepository()
        tracking_repo = TrackingRepository()

        tracking_number = f"TRK{random.randint(100000, 999999)}"

        shipment = Shipment(
            tracking_number=tracking_number,
            customer_id=user.id,
            source_address=data.source_address,
            destination_address=data.destination_address,
            status="CREATED"
        )

        shipment = repo.create(db, shipment)

        tracking = Tracking(
            shipment_id=shipment.id,
            location=data.source_address,
            status="CREATED"
        )

        tracking_repo.create(db, tracking)

        return shipment

    def update_status(self, db: Session, tracking_number: str, status: str, user):
        repo = ShipmentRepository()
        tracking_repo = TrackingRepository()

        shipment = repo.get_by_tracking(db, tracking_number)

        if not shipment:
            raise HTTPException(status_code=404, detail="Shipment not found")

        shipment.status = status
        db.commit()

        tracking = Tracking(
            shipment_id=shipment.id,
            location="Updated",
            status=status
        )

        tracking_repo.create(db, tracking)

        return shipment

    def cancel_shipment(self, db: Session, tracking_number: str, user):
        repo = ShipmentRepository()

        shipment = repo.get_by_tracking(db, tracking_number)

        if not shipment:
            raise HTTPException(status_code=404, detail="Shipment not found")

        if shipment.status == "DELIVERED":
            raise HTTPException(status_code=400, detail="Cannot cancel delivered shipment")

        shipment.status = "CANCELLED"
        db.commit()

        return shipment

    def get_shipment(self, db: Session, tracking_number: str, user=None):
        repo = ShipmentRepository()
        shipment = repo.get_by_tracking(db, tracking_number)

        if not shipment:
            raise HTTPException(status_code=404, detail="Shipment not found")

        if user and user.role.value == "customer" and shipment.customer_id != user.id:
            raise HTTPException(
                status_code=403,
                detail="You do not have permission to view this shipment"
            )

        return shipment