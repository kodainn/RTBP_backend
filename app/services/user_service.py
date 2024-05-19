from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.users import CreateUser, OutputUser

class UserService:
    def __init__(self, session: Session):
        self.user_repository = UserRepository(session)
    

    def create(self, req_body: CreateUser) -> OutputUser:
        output_user = self.user_repository.create(req_body)
        return output_user