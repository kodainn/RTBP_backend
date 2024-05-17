from typing import List
from pydantic import BaseModel
from datetime import date

class StudiedHistoryBook(BaseModel):
    id:            int
    title:         str
    img_url:       str
    studied_count: int

class ListStudiedHistoryBooks(BaseModel):
    studied_history_books: List[StudiedHistoryBook]


class TargetItem(BaseModel):
        id:           int
        description:  str
        is_complated: bool

class StudiedHistory(BaseModel):
    id:           int
    start_on:     date
    target_on:    date
    target_items: List[TargetItem]
    memo:         str
    study_minutes:  int

class ListStudiedHistories(BaseModel):
    studied_histories: List[StudiedHistory]