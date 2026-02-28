from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import timedelta

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:

    def register(self, db: Session, data):
        repo = UserRepository()

        existing = repo.get_by_email(db, data.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        user = User(
            email=data.email,
            password_hash=hash_password(data.password),
            role=data.role
        )

        return repo.create(db, user)

    def login(self, db: Session, email: str, password: str):
        repo = UserRepository()
        user = repo.get_by_email(db, email)

        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token(
            data={"sub": str(user.id), "role": user.role.value}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }