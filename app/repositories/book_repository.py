from datetime import date

from typing import Optional, List, Dict
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.model.models import Book, Shelve
from app.schemas.books import CreateBook



class BookRepository:
    def __init__(self, session: Session):
        self.session = session

    
    def user_has_find_by_id(self, user_id: int, id: int) -> Book:
        query = self.session.query(Book)
        query = query.filter_by(id=id, user_id=user_id, is_deleted=False)

        result = query.first()

        return result


    def user_has_count(self, user_id: int) -> int:
        query = self.session.query(Book)
        query = query.filter_by(user_id=user_id, is_deleted=False)

        result = query.count()

        return result
    

    def user_has_count_list_by_shelve(self, user_id: int) -> List:
        query = self.session.query(
                Shelve.name.label("shelve_name"),
                func.count(Book.id).label("book_count")
            )
        query = query.join(Book, Book.shelve_id == Shelve.id)
        query = query.filter_by(user_id=user_id, is_deleted=False)
        query = query.group_by("shelve_name")
        query = query.order_by("shelve_name")
        
        result = query.all()

        return result
    

    def user_has_has_book_by_title(self, user_id: int, title: str) -> bool:
        query = self.session.query(Book)
        query = query.filter_by(user_id=user_id, title=title, is_deleted=False)

        result = query.first()

        return result is not None
    

    def create(self, user_id: int, create_book: CreateBook) -> Book:
        book = Book(
                isbn=create_book.isbn,
                title=create_book.title,
                remark=create_book.remark,
                img_url=create_book.img_url,
                user_id=user_id,
                shelve_id=create_book.shelve_id
            )
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)

        return book