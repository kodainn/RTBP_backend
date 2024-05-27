from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class StudiedHistoryBook(BaseModel):
    book_id:       int
    title:         str
    img_url:       str
    studied_count: int

    class Config:
        orm_mode = True


class ListStudiedHistoryBooks(BaseModel):
    studied_history_books: List[Optional[StudiedHistoryBook]]


class TargetItem(BaseModel):
        id:           int
        description:  str
        is_completed: bool

        class Config:
            orm_mode = True

class StudiedHistory(BaseModel):
    id:            int
    start_on:      date
    target_on:     date
    target_items:  List[Optional[TargetItem]]
    memo:          str
    study_minutes: int

    class Config:
        orm_mode = True


class Book(BaseModel):
    id:           int
    shelve_name:  str
    title:        str
    remark:       str
    img_url:      str

    class Config:
        orm_mode = True


class InvidualStudiedHistoryBook(BaseModel):
    book:              Book
    studied_histories: List[Optional[StudiedHistory]]