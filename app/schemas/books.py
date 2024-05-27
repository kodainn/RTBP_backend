from pydantic import BaseModel, Field


class OutputBook(BaseModel):
    id:           int
    shelve_name:  str
    title:        str
    remark:       str
    img_url:      str

    class Config:
        orm_mode = True


class CreateBook(BaseModel):
    title:     str = Field(min_length=1, max_length=50)
    shelve_id: int
    remark:    str = Field(max_length=255)
    img_url:   str


class UpdateBook(BaseModel):
    title:   str = Field(min_length=1, max_length=50)
    remark:  str = Field(max_length=255)
    img_url: str
