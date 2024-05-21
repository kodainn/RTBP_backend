from datetime import date

from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func, exists, and_, cast, Integer

from app.database.model.models import StudyingBook, StudyTrack


class StudyTrackRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def user_has_total_minutes(self, user_id: int) -> int:
        query = self.session.query(func.sum(StudyTrack.minutes).label("user_total_minutes"))
        query = query.filter(
                exists().where(
                    and_(StudyTrack.studying_book_id == StudyingBook.id, StudyingBook.user_id == user_id)
                )
            )
        
        result = query.first()
        
        if result["user_total_minutes"] is None:
            return 0
        
        return result["user_total_minutes"]
    

    def user_has_monthly_total_by_year(self, year: int, user_id: int) -> List:
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        
        query = self.session.query(
                cast(func.to_char(StudyTrack.study_on, 'YYYY'), Integer).label('year'),
                cast(func.to_char(StudyTrack.study_on, 'MM'), Integer).label('month'),
                func.sum(StudyTrack.minutes).label('study_minutes')
            )
        query = query.filter(
            exists().where(
                and_(StudyTrack.studying_book_id == StudyingBook.id, StudyingBook.user_id == user_id)
            ),
            StudyTrack.study_on >= start_date,
            StudyTrack.study_on <= end_date
            )
        query = query.group_by('year', 'month')
        query = query.order_by('year', 'month')
        
        result = query.all()
        
        return result