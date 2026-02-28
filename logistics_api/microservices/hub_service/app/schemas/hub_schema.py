from pydantic import BaseModel


class HubCreate(BaseModel):
    name: str
    location: str


class HubResponse(BaseModel):
    id: int
    name: str
    location: str

    class Config:
        from_attributes = True