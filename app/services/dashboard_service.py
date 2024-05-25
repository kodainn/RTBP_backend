from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.studying_book_repository import StudyingBookRepository
from app.repositories.study_track_repository import StudyTrackRepository
from app.repositories.book_repository import BookRepository
from app.schemas.dashboard import StudyBookProgress, StudyTimes, BookCounts
from app.database.model.models import User
import app.utils.datetime_jp as datetime_jp

class DashboardService:
    def __init__(self, session: Session, user: User):
        self.studying_book_repository = StudyingBookRepository(session)
        self.study_track_repository = StudyTrackRepository(session)
        self.book_repository = BookRepository(session)
        self.user = user
    

    def studying_book_progress(self) -> StudyBookProgress:
        period_on = datetime_jp.now_date()
        complate_count = self.studying_book_repository.user_with_complated_count_in_period(period_on, self.user.id)
        incomplete_count = self.studying_book_repository.user_with_incompleted_count_in_period(period_on, self.user.id)
        period = self.studying_book_repository.user_with_period(period_on, self.user.id)

        return StudyBookProgress(
            study_books_completed_count=complate_count,
            study_books_incomplete_count=incomplete_count,
            start_study_period_on=period["start_study_period_on"],
            end_study_period_on=period["end_study_period_on"]
        )
    
    
    def study_times(self) -> StudyTimes:
        total_minutes = self.study_track_repository.user_with_total_minutes(self.user.id)
        now_year = datetime_jp.now_year()
        monthly_total_by_year = self.study_track_repository.user_with_monthly_total_by_year(now_year, self.user.id)
        
        return StudyTimes(
            study_minutes_total=total_minutes,
            study_minutes_by_monthly=monthly_total_by_year
        )
    

    def book_counts(self) -> BookCounts:
        book_count = self.book_repository.user_with_count(self.user.id)
        book_count_by_shelve = self.book_repository.user_with_count_list_by_shelve(self.user.id)

        return BookCounts(
            book_total_count=book_count,
            book_count_by_shelve=book_count_by_shelve
        )