from sqlalchemy import Column, String, ForeignKey, Text, Integer
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Shipment(BaseModel):
    __tablename__ = "shipments"

    tracking_number = Column(String, unique=True, nullable=False)
    source_address = Column(Text, nullable=False)
    destination_address = Column(Text, nullable=False)
    status = Column(String, default="created")

    customer_id = Column(Integer, ForeignKey("users.id"))
    agent_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    hub_id = Column(Integer, ForeignKey("hubs.id"), nullable=True)

    customer = relationship("User", foreign_keys=[customer_id])