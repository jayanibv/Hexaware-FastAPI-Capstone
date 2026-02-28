import random
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.shipment import Shipment


class ShipmentService:

    def create_shipment(self, db: Session, user_id: int, data):
        tracking_number = f"TRK{random.randint(100000, 999999)}"

        shipment = Shipment(
            tracking_number=tracking_number,
            source_address=data.source_address,
            destination_address=data.destination_address,
            status="CREATED",
            customer_id=user_id
        )

        db.add(shipment)
        db.commit()
        db.refresh(shipment)

        return shipment

    def get_shipment(self, db: Session, tracking_number: str):
        shipment = db.query(Shipment).filter(
            Shipment.tracking_number == tracking_number
        ).first()

        if not shipment:
            raise HTTPException(status_code=404, detail="Shipment not found")

        return shipment

    def update_status(self, db: Session, tracking_number: str, status: str):
        shipment = db.query(Shipment).filter(
            Shipment.tracking_number == tracking_number
        ).first()

        if not shipment:
            raise HTTPException(status_code=404, detail="Shipment not found")

        shipment.status = status
        db.commit()
        db.refresh(shipment)

        return shipment