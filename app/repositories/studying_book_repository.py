from datetime import date

from typing import Dict, Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.model.models import StudyingBook
from app.schemas.studying_books import CreateStudyingBook
from app.utils.datetime_jp import now_date



class StudyingBookRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def user_has_complated_count_in_period(self, period_on: date, user_id: int) -> int:
        query = self.session.query(StudyingBook)
        query = query.filter(
                StudyingBook.user_id == user_id,
                StudyingBook.start_on <= period_on,
                StudyingBook.target_on >= period_on,
                StudyingBook.is_complated == True,
                StudyingBook.is_deleted == False
            )
        
        result = query.count()

        return result

    
    def user_has_incompleted_count_in_period(self, period_on: date, user_id: int) -> int:
        query = self.session.query(StudyingBook)
        query = query.filter(
                StudyingBook.user_id == user_id,
                StudyingBook.start_on <= period_on,
                StudyingBook.target_on >= period_on,
                StudyingBook.is_complated == False,
                StudyingBook.is_deleted == False
            )
        
        result = query.count()

        return result
    

    def user_has_period(self, period_on: date, user_id: int) -> Dict:
        query = self.session.query(
                func.min(StudyingBook.start_on).label("start_study_period_on"),
                func.max(StudyingBook.target_on).label('end_study_period_on')
            )
        query = query.filter(
                StudyingBook.user_id == user_id,
                StudyingBook.start_on <= period_on,
                StudyingBook.target_on >= period_on,
                StudyingBook.is_deleted == False
            )
        
        result = query.first()
        
        return result
    

    def user_has_find_by_id(self, user_id: int, id: int):
        query = self.session.query(StudyingBook)
        query = query.filter_by(user_id=user_id, id=id, is_deleted=False)

        result = query.first()

        return result
    

    def user_has_list(self, user_id: int) -> List[Optional[StudyingBook]]:
        query = self.session.query(StudyingBook)
        query = query.filter_by(user_id=user_id, is_complated=False, is_deleted=False)

        result = query.all()

        return result


    def create(self, user_id: int, create_studying_book: CreateStudyingBook) -> StudyingBook:
        start_on = now_date()

        studying_book = StudyingBook(
            start_on=start_on,
            target_on=create_studying_book.target_on,
            user_id=user_id,
            book_id=create_studying_book.book_id
        )

        self.session.add(studying_book)
        self.session.flush()
        self.session.refresh(studying_book)

        return studying_book
    

    def delete(self, user_id: int, id: int) -> None:
        query = self.session.query(StudyingBook)
        query = query.filter_by(user_id=user_id, id=id, is_deleted=False)
        
        result = query.first()
        result.user_id = user_id
        result.is_deleted = True
        self.session.commit()

        return