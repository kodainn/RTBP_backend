import hashlib, random, string, datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import get_env_value
from database.model.models import User, Shelve, Book, StudyingBook, TargetItem, StudyTrack


def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)


def seeder() -> None:
    engine = create_engine(str(get_env_value("DATABASE_URL")), echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    user_id = 1
    users = []
    shelves = []
    books = []
    studying_books = []
    target_items = []
    study_tracks = []
    
    start_on = datetime.date(2024, 5, 11)
    plus_day = 0

    users.append({
        "id": user_id,
        "name": randomname(10),
        "email": "test@example.com",
        "password": hashlib.sha256("password".encode()).hexdigest()
    })

    for shelve_id in range(1, 6):
        shelves.append({
            "id": shelve_id,
            "name": randomname(10),
            "user_id": user_id
        })

        for book_id in range(1, 11):
            book_id = (shelve_id - 1) * 10 + book_id
            books.append({
                "id": book_id,
                "isbn": "1111111111111",
                "title": randomname(10),
                "remark": randomname(30),
                "img_url": "https://ebookstore.sony.jp/photo/LT00014922/LT000149223001280076_XLARGE.jpg",
                "user_id": user_id,
                "shelve_id": shelve_id
            })

            for studying_book_id in range(1,3):
                studying_book_id = (book_id - 1) * 10 + studying_book_id
                studying_books.append({
                    "id": studying_book_id,
                    "memo": randomname(10),
                    "start_on": "2024-05-11",
                    "target_on": "2024-06-11",
                    "user_id": user_id,
                    "book_id": book_id
                })

                for target_item_id in range(1, 3):
                    target_item_id = (studying_book_id - 1) * 10 + target_item_id
                    target_items.append({
                        "id": target_item_id,
                        "description": randomname(10),
                        "studying_book_id": studying_book_id
                    })
                
                for study_track_id in range(1, 6):
                    study_track_id = (studying_book_id - 1) * 10 + study_track_id
                    study_tracks.append({
                        "id": study_track_id,
                        "minutes": random.randint(0, 100),
                        "study_on": start_on + datetime.timedelta(days=plus_day),
                        "studying_book_id": studying_book_id
                    })
                    plus_day += 1

    try:
        with session.begin():
            session.bulk_insert_mappings(User, users)
            session.bulk_insert_mappings(Shelve, shelves)
            session.bulk_insert_mappings(Book, books)
            session.bulk_insert_mappings(StudyingBook, studying_books)
            session.bulk_insert_mappings(TargetItem, target_items)
            session.bulk_insert_mappings(StudyTrack, study_tracks)
            session.commit()
    except Exception as e:
        print("えらーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー:", e)
        session.rollback()
    finally:
        session.close()