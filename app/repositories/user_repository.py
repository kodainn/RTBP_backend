from typing import Optional
from sqlalchemy.orm import Session

from app.database.model.models import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def find_by_username(self, username: str) -> Optional[User]:
        if not username:
            return None
        
        user = self.session.query(User).filter_by(name=username).first()

        return user
    