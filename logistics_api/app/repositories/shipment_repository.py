from sqlalchemy.orm import Session
from app.models.shipment import Shipment


class ShipmentRepository:

    def create(self, db: Session, shipment: Shipment):
        db.add(shipment)
        db.commit()
        db.refresh(shipment)
        return shipment

    def get_by_tracking(self, db: Session, tracking_number: str):
        return db.query(Shipment).filter(
            Shipment.tracking_number == tracking_number
        ).first()

    def get_by_id(self, db: Session, shipment_id):
        return db.query(Shipment).filter(
            Shipment.id == shipment_id
        ).first()

    def get_all(self, db: Session):
        return db.query(Shipment).all()

    def delete(self, db: Session, shipment: Shipment):
        db.delete(shipment)
        db.commit()