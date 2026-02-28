from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.hub_schema import HubCreate, HubResponse
from app.services.hub_service import HubService
from app.dependencies import require_role, get_current_user

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
    user_id: int = Depends(require_role(["ADMIN"]))
):
    return HubService().create_hub(db, data)


@router.get("", response_model=list[HubResponse])
def get_hubs(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return HubService().get_all_hubs(db)


@router.delete("/{hub_id}")
def delete_hub(
    hub_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(require_role(["ADMIN"]))
):
    return HubService().delete_hub(db, hub_id)