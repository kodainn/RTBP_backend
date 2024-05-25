from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth import CreateToken, Token
from app.utils.auth import create_access_token
from app.utils.auth_password import vertify_password
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, session: Session):
        self.user_repository = UserRepository(session)


    def create_access_token(self, req_body: CreateToken) -> Token:
        user = self.user_repository.find_by_username(req_body.name)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found."
            )
        
        if not vertify_password(user.password, req_body.password):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Password is incorrect."
            )
        
        accsess_token = create_access_token(user.name)
        return Token(access_token=accsess_token, token_type="bearer")