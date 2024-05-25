from datetime import date

from typing import Optional, List, Dict
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.model.models import Book, Shelve, StudyingBook
from app.schemas.books import CreateBook, UpdateBook



class BookRepository:
    def __init__(self, session: Session):
        self.session = session

    
    def user_with_find_by_id(self, user_id: int, id: int) -> Optional[Book]:
        query = self.session.query(Book)
        query = query.filter_by(id=id, user_id=user_id)

        result = query.first()

        return result


    def user_with_count(self, user_id: int) -> int:
        query = self.session.query(Book)
        query = query.filter_by(user_id=user_id)

        result = query.count()

        return result
    

    def user_with_count_list_by_shelve(self, user_id: int) -> List:
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
    

    def user_with_has_book_by_title(self, user_id: int, title: str) -> bool:
        query = self.session.query(Book)
        query = query.filter_by(user_id=user_id, title=title)

        result = query.first()

        return result is not None
    

    def user_with_has_some_book_by_title(self, user_id: int, id: int, title: str) -> bool:
        query = self.session.query(Book)
        query = query.filter(Book.user_id==user_id, Book.id != id, Book.title == title)

        result = query.first()

        return result is not None
    

    def user_with_individual_by_id(self, user_id: int, id: int) -> Optional[Book]:
        query = self.session.query(Book)
        query = query.filter_by(user_id=user_id, id=id)

        result = query.first()

        return result
    

    def user_with_complated_in_count_list(self, user_id: int) -> List[Optional[Dict]]:
        query = self.session.query(Book.id, Book.title, Book.img_url, func.count(StudyingBook.id).label("studied_count"))
        query = query.join(Book, Book.id == StudyingBook.book_id)
        query = query.filter(Book.user_id == user_id, StudyingBook.is_completed == True)
        query = query.group_by(Book.id, Book.title, Book.img_url)

        result = query.all()

        return result


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
    

    def update(self, user_id: int, id: int, update_book: UpdateBook) -> Book:
        query = self.session.query(Book)
        query = query.filter_by(user_id=user_id, id=id)

        result = query.first()
        result.isbn = update_book.isbn
        result.title = update_book.title
        result.remark = update_book.remark
        result.img_url = update_book.img_url
        result.user_id = user_id,

        self.session.commit()
        
        return result
    

    def delete(self, user_id: int, id: int) -> None:
        query = self.session.query(Book)
        query = query.filter_by(user_id=user_id, id=id)

        query.delete()

        self.session.commit()

        return