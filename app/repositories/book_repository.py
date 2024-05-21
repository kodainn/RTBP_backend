from datetime import date

from typing import Optional, List, Dict
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.model.models import Book, Shelve



class BookRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def user_has_count(self, user_id: int) -> int:
        query = self.session.query(Book)
        query = query.filter_by(user_id=user_id)

        result = query.count()

        return result
    

    def user_has_count_list_by_shelve(self, user_id: int) -> List:
        query = self.session.query(
                Shelve.name.label("shelve_name"),
                func.count(Book.id).label("book_count")
            )
        query = query.join(Book, Book.shelve_id == Shelve.id)
        query = query.filter_by(user_id=user_id)
        query = query.group_by("shelve_name")
        query = query.order_by("shelve_name")
        
        result = query.all()

        return result