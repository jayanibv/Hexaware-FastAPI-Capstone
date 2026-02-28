from sqlalchemy.orm import Session
from app.models.hub import Hub


class HubRepository:

    def create(self, db: Session, hub: Hub):
        db.add(hub)
        db.commit()
        db.refresh(hub)
        return hub

    def get_by_id(self, db: Session, hub_id):
        return db.query(Hub).filter(
            Hub.id == hub_id
        ).first()

    def get_all(self, db: Session):
        return db.query(Hub).all()