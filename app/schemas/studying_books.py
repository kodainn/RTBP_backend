from datetime import date
from typing import List
from pydantic import BaseModel


class StudyingBook(BaseModel):
    id:        int
    title:     str
    img_url:   str
    start_on:  date
    target_on: date

class ListStudyingBooks(BaseModel):
    studying_books: List[StudyingBook]


class TargetItem(BaseModel):
    id:           int
    description:  str
    is_complated: bool

class IndividualStudyingBook(BaseModel):
    id:           int
    start_on:     date
    target_on:    date
    target_items: List[TargetItem]


class CrateTargetItem(BaseModel):
    description: str

class CreateStudyingBook(BaseModel):
    book_id:      int
    target_items: List[CrateTargetItem]
    target_on:    date


class CreateComplateTargetItem(BaseModel):
    id:           int
    is_complated: bool

class CreateStudyingBookRecord(BaseModel):
    target_complate_items: List[CreateComplateTargetItem]
    study_minutes:  int