from app.models.hub import Hub

class HubService:

    def create_hub(self, db, data):
        hub = Hub(name=data.name, location=data.location)
        db.add(hub)
        db.commit()
        db.refresh(hub)
        return hub

    def list_hubs(self, db):
        return db.query(Hub).all()