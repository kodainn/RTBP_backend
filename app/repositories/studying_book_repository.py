from datetime import date

from typing import Dict, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.model.models import StudyingBook



class StudyingBookRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def complated_count_in_period_by_user_id(self, period_on: date, user_id: int) -> int:
        count = self.session.query(StudyingBook).filter(
                StudyingBook.user_id == user_id,
                StudyingBook.start_on <= period_on,
                StudyingBook.target_on >= period_on,
                StudyingBook.is_complated == True,
                StudyingBook.is_deleted == False
            ).count()

        return count

    
    def incomplete_count_in_period_by_user_id(self, period_on: date, user_id: int) -> int:
        count = self.session.query(StudyingBook).filter(
                StudyingBook.user_id == user_id,
                StudyingBook.start_on <= period_on,
                StudyingBook.target_on >= period_on,
                StudyingBook.is_complated == False,
                StudyingBook.is_deleted == False
            ).count()

        return count
    

    def period_by_user_id(self, period_on: date, user_id: int) -> Dict[str, date]:
        query = self.session.query(
                func.min(StudyingBook.start_on).label("start_study_period_on"),
                func.max(StudyingBook.target_on).label('end_study_period_on')
            ).filter(
                StudyingBook.user_id == user_id,
                StudyingBook.start_on <= period_on,
                StudyingBook.target_on >= period_on,
                StudyingBook.is_complated == False,
                StudyingBook.is_deleted == False
            ).group_by(StudyingBook.user_id)
        
        period = query.first()

        return period