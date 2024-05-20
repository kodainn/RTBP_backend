from datetime import date

from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.model.models import Book, Shelve
from app.schemas.dashboard import BookCountsByShelve



class BookRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def has_user_count(self, user_id: int) -> int:
        count = self.session.query(
                Book
            ).filter_by(
                user_id=user_id
            ).count()

        return count
    

    def has_user_count_by_shelve(self, user_id: int) -> List[Optional[BookCountsByShelve]]:
        count_by_shelve = self.session.query(
                Shelve.name.label("shelve_name"),
                func.count(Book.id).label("book_count")
            ).join(
                Book, Book.shelve_id == Shelve.id
            ).filter_by(
                user_id=user_id
            ).group_by(
                "shelve_name"
            ).order_by(
                "shelve_name"
            ).all()
        
        return count_by_shelve