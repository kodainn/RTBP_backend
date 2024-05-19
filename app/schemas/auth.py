from pydantic import BaseModel, Field


class CreateToken(BaseModel):
    name:     str
    password: str


class Token(BaseModel):
    access_token: str
    token_type:   str

class Register(BaseModel):
    name:     str
    email:    str
    password: str