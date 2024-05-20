from typing import List, Optional
from pydantic import BaseModel

class Shelve(BaseModel):
    id:   int
    name: str

class Book(BaseModel):
    id:      int
    title:   str
    img_url: str

class ShelveInListBooks(BaseModel):
    id:    int
    name:  str
    books: List[Optional[Book]]


class ListShelves(BaseModel):
    shelves: List[Optional[ShelveInListBooks]]


class CreateShelve(BaseModel):
    name: str


class UpdateShelve(BaseModel):
    id:   int
    name: str