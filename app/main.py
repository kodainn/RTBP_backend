from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.dashboard import router as dashboard_router
from app.routers.books import router as books_router
from app.routers.shelves import router as shelves_router
from app.routers.studied_history_books import router as studied_history_books_router
from app.routers.studying_books import router as studying_books_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://tech-books-study.vercel.app"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(dashboard_router)
app.include_router(books_router)
app.include_router(shelves_router)
app.include_router(studied_history_books_router)
app.include_router(studying_books_router)

