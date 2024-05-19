from pydantic import BaseModel


class CreateToken(BaseModel):
    name:     str
    password: str


class Token(BaseModel):
    access_token: str
    token_type:   str