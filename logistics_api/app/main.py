from fastapi import FastAPI
from app.core.database import engine
from app.core.database import Base

from app.models import user, shipment, tracking, hub

from app.api.routes import auth, shipments, hub

app = FastAPI(title="Logistics API - Sprint 1")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(shipments.router)
app.include_router(hub.router)