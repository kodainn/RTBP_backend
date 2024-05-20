from datetime import date

from typing import Dict, Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import func, exists, select, and_, cast, Integer

from app.database.model.models import StudyingBook, StudyTrack
from app.schemas.dashboard import StudyTimesByMonthly


class StudyTrackRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def total_minutes_by_user_id(self, user_id: int) -> int:
        user_total = self.session.query(
                func.sum(StudyTrack.minutes).label("user_total_minutes")
            ).filter(
                exists().where(and_(StudyTrack.studying_book_id == StudyingBook.id, StudyingBook.user_id == user_id))
            ).first()
        if user_total["user_total_minutes"] is None:
            return 0
        
        return user_total["user_total_minutes"]
    

    def monthly_total_by_year_by_user_id(self, year: int, user_id: int) -> List[Optional[StudyTimesByMonthly]]:
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        
        study_tracks = self.session.query(
                cast(func.to_char(StudyTrack.study_on, 'YYYY'), Integer).label('year'),
                cast(func.to_char(StudyTrack.study_on, 'MM'), Integer).label('month'),
                func.sum(StudyTrack.minutes).label('study_minutes')
            ).filter(
            exists().where(
                and_(StudyTrack.studying_book_id == StudyingBook.id, StudyingBook.user_id == user_id)
            ),
            StudyTrack.study_on >= start_date,
            StudyTrack.study_on <= end_date
            ).group_by(
                'year', 'month'
            ).order_by(
                'year', 'month'
            ).all()
        
        return study_tracks