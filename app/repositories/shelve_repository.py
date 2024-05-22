from datetime import date

from typing import Optional, List
from sqlalchemy.orm import Session, selectinload, load_only

from app.database.model.models import Shelve
from app.schemas.shelves import CreateShelve, UpdateShelve



class ShelveRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def user_has_list(self, user_id: int) -> List:
        query = self.session.query(Shelve)
        query = query.options(load_only('id', 'name'))
        query = query.options(selectinload(Shelve.books).load_only('id', 'title', 'img_url'))        
        query = query.filter_by(user_id=user_id, is_deleted=False)

        result = query.all()
    
        return result
    

    def user_has_shelve_in_books(self, user_id: int, id: int) -> Optional[Shelve]:
        query = self.session.query(Shelve)
        query = query.options(load_only('id', 'name'))
        query = query.options(selectinload(Shelve.books).load_only('id', 'title', 'img_url'))        
        query = query.filter_by(user_id=user_id, id=id, is_deleted=False)

        result = query.first()
    
        return result
    
    
    def user_has_individual_by_id(self, user_id: int, id: int) -> Optional[Shelve]:
        query = self.session.query(Shelve)
        query = query.filter_by(user_id=user_id, id=id, is_deleted=False)

        result = query.first()

        return result

    
    def user_has_has_shelve_by_name(self, user_id: int, name: str) -> bool:
        query = self.session.query(Shelve)
        query = query.filter_by(user_id=user_id, name=name, is_deleted=False)

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
        query = query.filter_by(user_id=user_id, id=id, is_deleted=False)

        result = query.first()
        result.name = update_shelve.name
        result.user_id = user_id

        self.session.commit()
        
        return result
    

    def delete(self, user_id: int, id: int) -> None:
        query = self.session.query(Shelve)
        query = query.filter_by(user_id=user_id, id=id, is_deleted=False)

        result = query.first()
        result.user_id = user_id
        result.is_deleted = True

        self.session.commit()