from sqlalchemy import Column, String, ForeignKey, Integer
from app.models.base import BaseModel


class Tracking(BaseModel):
    __tablename__ = "tracking_updates"

    shipment_id = Column(Integer, ForeignKey("shipments.id"))
    location = Column(String)
    status = Column(String)