from datetime import date

from typing import Dict, Optional, Union
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.model.models import StudyingBook



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