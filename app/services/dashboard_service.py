from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.studying_book_repository import StudyingBookRepository
from app.repositories.study_track_repository import StudyTrackRepository
from app.schemas.dashboard import StudyBookProgress, StudyTimes
from app.database.model.models import User
import app.utils.datetime_jp as datetime_jp

class DashboardService:
    def __init__(self, session: Session, user: User):
        self.studying_book_repository = StudyingBookRepository(session)
        self.study_track_repository = StudyTrackRepository(session)
        self.user = user
    

    def studying_book_progress(self) -> StudyBookProgress:
        period_on = datetime_jp.now_date()
        complate_count = self.studying_book_repository.complated_count_in_period_by_user_id(period_on, self.user.id)
        incomplete_count = self.studying_book_repository.incomplete_count_in_period_by_user_id(period_on, self.user.id)
        period = self.studying_book_repository.period_by_user_id(period_on, self.user.id)

        return StudyBookProgress(
            study_books_completed_count=complate_count,
            study_books_incomplete_count=incomplete_count,
            start_study_period_on=period["start_study_period_on"],
            end_study_period_on=period["end_study_period_on"]
        )
    
    
    def study_times(self) -> StudyTimes:
        total_minutes = self.study_track_repository.total_minutes_by_user_id(self.user.id)
        monthly_total_by_year = self.study_track_repository.monthly_total_by_year_by_user_id(2024, self.user.id)
        
        return StudyTimes(
            study_minutes_total=total_minutes,
            study_minutes_by_monthly=monthly_total_by_year
        )