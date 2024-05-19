from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.users import CreateUser, OutputUser
from app.database.config.connect import get_db
from app.services.user_service import UserService

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=OutputUser)
async def register(req_body: CreateUser, session: Session = Depends(get_db)):
    output_user = UserService(session).create(req_body)
    return output_user