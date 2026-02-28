from pydantic import BaseModel
from uuid import UUID


class TrackingCreate(BaseModel):
    location: str
    status: str


class TrackingResponse(BaseModel):
    id: int
    shipment_id: int
    location: str
    status: str

    class Config:
        from_attributes = True