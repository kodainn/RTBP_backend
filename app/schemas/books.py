from typing import Union
from pydantic import BaseModel


class Book(BaseModel):
    id:           int
    isnb:         int
    shelve_name:  str
    title:        str
    remark:       Union[str, None]
    img_url:      Union[str, None]


class CreateBook(BaseModel):
    isbn:         int
    title:        str
    shelve_id:    int
    remark:       Union[str, None]
    img_url:      Union[str, None]


class UpdateBook(BaseModel):
    id:           int
    isbn:         int
    title:        str
    remark:       Union[str, None]
    img_url:      Union[str, None]
