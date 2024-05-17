from fastapi import FastAPI
from app.routers.auth import router as auth_router # type: ignore
from app.routers.dashboard import router as dashboard_router # type: ignore
from app.routers.books import router as books_router # type: ignore
from app.routers.shelves import router as shelves_router # type: ignore
from app.routers.studied_history_books import router as studied_history_books_router # type: ignore
from app.routers.studying_books import router as studying_books_router # type: ignore

app = FastAPI()

app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(books_router)
app.include_router(shelves_router)
app.include_router(studied_history_books_router)
app.include_router(studying_books_router)

