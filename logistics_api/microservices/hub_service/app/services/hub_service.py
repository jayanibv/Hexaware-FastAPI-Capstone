from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.hub import Hub


class HubService:

    def create_hub(self, db: Session, data):
        hub = Hub(
            name=data.name,
            location=data.location
        )

        db.add(hub)
        db.commit()
        db.refresh(hub)

        return hub

    def get_all_hubs(self, db: Session):
        return db.query(Hub).all()

    def delete_hub(self, db: Session, hub_id: int):
        hub = db.query(Hub).filter(Hub.id == hub_id).first()

        if not hub:
            raise HTTPException(status_code=404, detail="Hub not found")

        db.delete(hub)
        db.commit()

        return {"message": "Hub deleted successfully"}