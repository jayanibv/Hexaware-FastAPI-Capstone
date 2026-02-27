import random
from app.models.shipment import Shipment
from app.models.tracking import Tracking

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