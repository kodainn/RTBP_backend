from datetime import date
from typing import List, Optional
from pydantic import BaseModel


class StudyBookProgress(BaseModel):
    study_books_completed_count:  int
    study_books_incomplete_count: int
    start_study_period_on:        Optional[date]
    end_study_period_on:          Optional[date]


class StudyTimesByMonthly(BaseModel):
    year:          int
    month:         int
    study_minutes: int

class StudyTimes(BaseModel):
    study_minutes_total:      int
    study_minutes_by_monthly: List[Optional[StudyTimesByMonthly]]


class BookCountsByShelve(BaseModel):
    shelve_name: str
    books_count: int

class BookCounts(BaseModel):
    books_total_count:      int
    books_count_by_shelve:  List[BookCountsByShelve]
