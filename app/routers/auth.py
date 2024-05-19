from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.auth import CreateToken, Token
from app.database.config.connect import get_db
from app.services.auth_service import AuthService


router = APIRouter()

@router.post("/token",response_model=Token, status_code=status.HTTP_201_CREATED)
async def token(req_body: CreateToken, session: Session = Depends(get_db)):
    access_token = AuthService(session).create_access_token(req_body)
    return access_token