from pydantic import BaseModel


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


class UpdateStatusRequest(BaseModel):
    status: str