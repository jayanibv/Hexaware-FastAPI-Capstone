from sqlalchemy.orm import Session
from app.models.tracking import Tracking


class TrackingRepository:

    def create(self, db: Session, tracking: Tracking):
        db.add(tracking)
        db.commit()
        db.refresh(tracking)
        return tracking

    def get_by_shipment(self, db: Session, shipment_id):
        return db.query(Tracking).filter(
            Tracking.shipment_id == shipment_id
        ).all()