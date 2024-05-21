from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.shelves import ListShelves, CreateShelve, OutputShelve
from app.database.model.models import User, Shelve
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
    

    def individual_shelve(self, id: int) -> OutputShelve:
        shelve = self.shelve_repository.user_has_individual_by_id(self.user.id, id)
        if shelve is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="その本棚は存在しません。"
            )
        
        return OutputShelve(
            id=shelve.id,
            name=shelve.name
        )

    def create(self, req_body: CreateShelve) -> OutputShelve:
        has_shelve = self.shelve_repository.user_has_has_shelve_by_shelve_name(self.user.id, req_body.name)
        if has_shelve:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="その棚名は既に登録されています。"
            )

        shelve = self.shelve_repository.create(req_body)

        return OutputShelve(
            id=shelve.id,
            name=shelve.name
        )