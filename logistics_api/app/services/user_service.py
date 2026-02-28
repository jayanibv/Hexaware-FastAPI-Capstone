from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.user_repository import UserRepository


class UserService:

    def get_all_users(self, db: Session):
        repo = UserRepository()
        return repo.get_all(db)

    def get_user(self, db: Session, user_id):
        repo = UserRepository()
        user = repo.get_by_id(db, user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user