from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_env_value

DB_URL = str(get_env_value("DATABASE_URL"))

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()