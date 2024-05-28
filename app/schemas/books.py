from pydantic import BaseModel, Field
from typing import Optional


class OutputBook(BaseModel):
    id:           int
    shelve_name:  str
    title:        str
    remark:       Optional[str]
    img_url:      Optional[str]

    class Config:
        orm_mode = True


class CreateBook(BaseModel):
    title:     str = Field(min_length=1, max_length=50)
    shelve_id: int
    remark:    Optional[str] = Field(max_length=200)
    img_url:   Optional[str]


class UpdateBook(BaseModel):
    title:   str = Field(min_length=1, max_length=50)
    remark:  Optional[str] = Field(max_length=200)
    img_url: Optional[str]
