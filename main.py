from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"hello": "hello"}