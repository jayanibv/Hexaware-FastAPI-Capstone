from datetime import datetime
from pydantic import BaseModel


# Base shared fields
class ShipmentBase(BaseModel):
    source_address: str
    destination_address: str


# Request model (what client sends)
class ShipmentCreate(ShipmentBase):
    pass


# Response model (what API returns)
class ShipmentResponse(ShipmentBase):
    id: int
    tracking_number: str
    status: str
    source_address: str
    destination_address: str
    created_at: datetime

    class Config:
        from_attributes = True
    
class ShipmentStatusUpdate(BaseModel):
    status: str