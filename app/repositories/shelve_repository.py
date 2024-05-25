from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import exists, and_

from app.database.model.models import Shelve, Book
from app.schemas.shelves import CreateShelve, UpdateShelve



class ShelveRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def user_with_list_in_book_like_title(self, user_id: int, title: str) -> List:
        query = self.session.query(Shelve)
        query = query.filter(
                Shelve.user_id == user_id,
                exists().where(
                    and_(Shelve.id == Book.shelve_id, Book.title.ilike("%" + title + "%"))
                )
            )

        result = query.all()
    
        return result
    

    def user_has_shelve_in_books(self, user_id: int, id: int) -> Optional[Shelve]:
        query = self.session.query(Shelve)      
        query = query.filter_by(user_id=user_id, id=id)

        result = query.first()
    
        return result
    
    
    def user_has_individual_by_id(self, user_id: int, id: int) -> Optional[Shelve]:
        query = self.session.query(Shelve)
        query = query.filter_by(user_id=user_id, id=id)

        result = query.first()

        return result

    
    def user_has_has_shelve_by_name(self, user_id: int, name: str) -> bool:
        query = self.session.query(Shelve)
        query = query.filter_by(user_id=user_id, name=name)

        result = query.first()

        return result is not None
    

    def create(self, user_id: int, create_shelve: CreateShelve) -> Shelve:
        shelve = Shelve(
            name=create_shelve.name,
            user_id=user_id,
        )
        self.session.add(shelve)
        self.session.commit()
        self.session.refresh(shelve)

        return shelve
    

    def update(self, user_id: int, id: int, update_shelve: UpdateShelve) -> Shelve:
        query = self.session.query(Shelve)
        query = query.filter_by(user_id=user_id, id=id)

        result = query.first()
        result.name = update_shelve.name
        result.user_id = user_id

        self.session.commit()
        
        return result
    

    def delete(self, user_id: int, id: int) -> None:
        query = self.session.query(Shelve)
        query = query.filter_by(user_id=user_id, id=id)

        query.delete()

        self.session.commit()

        return