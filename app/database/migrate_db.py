import os

from sqlalchemy import create_engine

from database.models import Base
from config import get_env_value
from database.seeding import seeding

engine = create_engine(str(get_env_value("DATABASE_URL")), echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    seeding()



if __name__ == "__main__":
    reset_database()
