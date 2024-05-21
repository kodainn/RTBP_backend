from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.shelves import ListShelves, ShelveInListBooks
from app.database.model.models import User
from app.repositories.shelve_repository import ShelveRepository


class ShelveService:
    def __init__(self, session: Session, user: User):
        self.shelve_repository = ShelveRepository(session)
        self.user = user


    def list_shelves(self) -> ListShelves:
        shelves = self.shelve_repository.user_has_list(self.user.id)

        return ListShelves(
            shelves=shelves
        )