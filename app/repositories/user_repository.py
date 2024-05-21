from typing import Optional
from sqlalchemy.orm import Session

from app.database.model.models import User
from app.schemas.users import CreateUser, OutputUser
from app.utils.auth_password import create_hash_password


class UserRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def find_by_username(self, username: str) -> Optional[User]:
        if not username:
            return None
        
        query = self.session.query(User)
        query = query.filter_by(name=username)
        
        result = query.first()

        return result
    
    
    def create(self, create_user: CreateUser) -> OutputUser:
        user = User(
            name=create_user.name,
            email=create_user.email,
            password=create_hash_password(create_user.password)
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return OutputUser(
            id=user.id,
            name=user.name,
            email=user.email
        )