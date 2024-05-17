from typing import Union
from pydantic import BaseModel


class Book(BaseModel):
    id:           int
    isnb:         int
    title:        str
    remark:       Union[str, None]
    img_url:      Union[str, None]


class CreateBook(BaseModel):
    isbn:         int
    title:        int
    remark:       Union[str, None]
    img_url:      Union[str, None]


class UpdateBook(BaseModel):
    isbn:         int
    title:        int
    remark:       Union[str, None]
    img_url:      Union[str, None]
