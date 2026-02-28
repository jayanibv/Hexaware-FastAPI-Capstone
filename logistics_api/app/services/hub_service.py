from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.hub import Hub
from app.repositories.hub_repository import HubRepository


class HubService:

    def create_hub(self, db: Session, data):
        repo = HubRepository()

        hub = Hub(
            hub_name=data.hub_name,
            city=data.city
        )

        return repo.create(db, hub)

    def get_all_hubs(self, db: Session):
        repo = HubRepository()
        return repo.get_all(db)