from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.tracking import Tracking


class TrackingService:

    def add_tracking(self, db: Session, data):
        tracking = Tracking(
            tracking_number=data.tracking_number,
            location=data.location,
            status=data.status
        )

        db.add(tracking)
        db.commit()
        db.refresh(tracking)

        return tracking

    def get_tracking_history(self, db: Session, tracking_number: str):
        history = db.query(Tracking).filter(
            Tracking.tracking_number == tracking_number
        ).all()

        if not history:
            raise HTTPException(status_code=404, detail="No tracking history found")

        return history