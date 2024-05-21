from datetime import date

from typing import Optional, List
from sqlalchemy.orm import Session, selectinload, load_only
from sqlalchemy import func

from app.database.model.models import Shelve
from app.schemas.shelves import CreateShelve



class ShelveRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def user_has_list(self, user_id: int) -> List:
        query = self.session.query(Shelve)
        query = query.options(load_only('id', 'name'))
        query = query.options(selectinload(Shelve.books).load_only('id', 'title', 'img_url'))        
        query = query.filter_by(user_id=user_id)

        result = query.all()
    
        return result
    
    
    def user_has_individual_by_id(self, user_id: str, id: int) -> Optional[Shelve]:
        query = self.session.query(Shelve)
        query = query.filter_by(user_id=user_id, id=id)

        result = query.first()

        return result

    
    def user_has_has_shelve_by_shelve_name(self, user_id: int, shelve_name: str) -> bool:
        query = self.session.query(Shelve)
        query = query.filter_by(user_id=user_id, name=shelve_name)

        result = query.first()

        return result is not None
    

    def create(self, create_shelve: CreateShelve) -> Shelve:
        shelve = Shelve(name=create_shelve.name)
        self.session.add(shelve)
        self.session.commit()
        self.session.refresh(shelve)

        return shelve