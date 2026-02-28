from pydantic import BaseModel


class TrackingCreate(BaseModel):
    tracking_number: str
    location: str
    status: str


class TrackingResponse(BaseModel):
    id: int
    tracking_number: str
    location: str
    status: str

    class Config:
        from_attributes = True