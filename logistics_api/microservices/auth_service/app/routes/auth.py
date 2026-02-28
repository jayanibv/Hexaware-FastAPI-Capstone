from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.auth_schema import RegisterRequest, LoginRequest
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    return AuthService().register(db, data)


from fastapi.security import OAuth2PasswordRequestForm


@router.post("/login")
def login(
    data: LoginRequest = None,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    if data:
        email = data.email
        password = data.password
    else:
        email = form_data.username
        password = form_data.password
        
    return AuthService().login(db, email, password)