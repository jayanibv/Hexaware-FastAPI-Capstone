import random
from app.models.shipment import Shipment
from app.models.tracking import Tracking
from fastapi import HTTPException


VALID_TRANSITIONS = {
    "created": ["in_transit"],
    "in_transit": ["out_for_delivery"],
    "out_for_delivery": ["delivered"],
    "delivered": []
}

class ShipmentService:

    def create_shipment(self, db, user, data):
        tracking_number = f"TRK{random.randint(100000, 999999)}"

        shipment = Shipment(
            tracking_number=tracking_number,
            customer_id=user.id,
            source_address=data.source_address,
            destination_address=data.destination_address,
            status="created"
        )

        db.add(shipment)
        db.commit()
        db.refresh(shipment)

        tracking = Tracking(
            shipment_id=shipment.id,
            location=data.source_address,
            status="created"
        )

        db.add(tracking)
        db.commit()

        return shipment

    def get_shipment_by_id(self, db, shipment_id):
        return db.query(Shipment).filter(
            Shipment.id == shipment_id
        ).first()

    def update_status(self, db, tracking_number, new_status, staff_id):
        shipment = db.query(Shipment).filter(
            Shipment.tracking_number == tracking_number
        ).first()

        if not shipment:
            raise HTTPException(404, "Shipment not found")

        if new_status not in VALID_TRANSITIONS[shipment.status]:
            raise HTTPException(400, "Invalid status transition")

        shipment.status = new_status
        db.commit()

        tracking = Tracking(
            shipment_id=shipment.id,
            location="Updated by staff",
            status=new_status
        )
        db.add(tracking)
        db.commit()
        return shipment


    def assign_hub(self, db, tracking_number, hub_id):
        shipment = db.query(Shipment).filter(
            Shipment.tracking_number == tracking_number
        ).first()

        if not shipment:
            raise HTTPException(404, "Shipment not found")

        shipment.hub_id = hub_id
        db.commit()
        db.refresh(shipment)

        return shipment