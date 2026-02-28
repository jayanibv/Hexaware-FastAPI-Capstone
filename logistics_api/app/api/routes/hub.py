from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, require_role
from app.services.hub_service import HubService
from app.schemas.hub_schema import HubCreate, HubResponse

router = APIRouter(prefix="/hubs", tags=["Hubs"])


@router.post("", response_model=HubResponse)
def create_hub(
    data: HubCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(["admin"]))
):
    return HubService().create_hub(db, data)

@router.get("", response_model=list[HubResponse])
def get_all_hubs(
    db: Session = Depends(get_db),
    user=Depends(require_role(["admin"]))
):
    return HubService().get_all_hubs(db)