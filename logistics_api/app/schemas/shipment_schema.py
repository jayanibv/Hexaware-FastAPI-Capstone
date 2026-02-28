from pydantic import BaseModel
from uuid import UUID


class ShipmentCreate(BaseModel):
    source_address: str
    destination_address: str


class ShipmentResponse(BaseModel):
    id: int
    tracking_number: str
    source_address: str
    destination_address: str
    status: str

    class Config:
        from_attributes = True


class ShipmentStatusUpdate(BaseModel):
    status: str
    location: str | None = None