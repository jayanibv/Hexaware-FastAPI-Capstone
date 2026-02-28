from pydantic import BaseModel
from uuid import UUID


class HubCreate(BaseModel):
    hub_name: str
    city: str


class HubResponse(BaseModel):
    id: int
    hub_name: str
    city: str

    class Config:
        from_attributes = True