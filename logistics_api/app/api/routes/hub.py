from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services.hub_service import HubService
from app.schemas.hub_schema import HubCreate, HubResponse
from app.core.dependencies import require_role

router = APIRouter(prefix="/hubs", tags=["Hubs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=HubResponse)
def create_hub(
    data: HubCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role("ADMIN"))
):
    return HubService().create_hub(db, data)

@router.get("", response_model=list[HubResponse])
def list_hubs(
    db: Session = Depends(get_db),
    user=Depends(require_role("ADMIN"))
):
    return HubService().list_hubs(db)