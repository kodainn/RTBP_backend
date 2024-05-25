
from sqlalchemy import Column, Integer,String, Boolean, Text, DateTime, Date, ForeignKey, func
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id            = Column(Integer, primary_key=True, autoincrement=True)
    name          = Column(String(50), nullable=False, unique=True)
    email         = Column(String(50), nullable=False, unique=True)
    password      = Column(String(255), nullable=False)
    created_at    = Column(DateTime, default=func.now())
    updated_at    = Column(DateTime, default=func.now(), onupdate=func.now())


class Shelve(Base):
    __tablename__ = 'shelves'

    id            = Column(Integer, primary_key=True, autoincrement=True)
    name          = Column(String(50), nullable=False, unique=True)
    user_id       = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    created_at    = Column(DateTime, default=func.now())
    updated_at    = Column(DateTime, default=func.now(), onupdate=func.now())

    books         = relationship("Book", backref="shelve")


class Book(Base):
    __tablename__  = 'books'

    id             = Column(Integer, primary_key=True, autoincrement=True)
    isbn           = Column(String(13))
    title          = Column(String(50), nullable=False)
    remark         = Column(String(255))
    img_url        = Column(Text)
    user_id        = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    shelve_id      = Column(Integer, ForeignKey("shelves.id", ondelete="CASCADE"))
    created_at     = Column(DateTime, default=func.now())
    updated_at     = Column(DateTime, default=func.now(), onupdate=func.now())

    studying_books = relationship("StudyingBook", backref="book")


class StudyingBook(Base):
    __tablename__ = 'studying_books'

    id            = Column(Integer, primary_key=True, autoincrement=True)
    memo          = Column(String(255))
    start_on      = Column(Date, nullable=False)
    target_on     = Column(Date, nullable=False)
    user_id       = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    book_id       = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    is_completed  = Column(Boolean, default=False)
    created_at    = Column(DateTime, default=func.now())
    updated_at    = Column(DateTime, default=func.now(), onupdate=func.now())

    target_items  = relationship("TargetItem", backref="studying_book")
    study_tracks  = relationship("StudyTrack", backref="studying_book")


class TargetItem(Base):
    __tablename__    = 'target_items'

    id               = Column(Integer, primary_key=True, autoincrement=True)
    description      = Column(String(255), nullable=False)
    is_completed     = Column(Boolean, default=False)
    studying_book_id = Column(Integer, ForeignKey("studying_books.id", ondelete="CASCADE"))
    created_at       = Column(DateTime, default=func.now())
    updated_at       = Column(DateTime, default=func.now(), onupdate=func.now())


class StudyTrack(Base):
    __tablename__    = 'study_tracks'

    id               = Column(Integer, primary_key=True, autoincrement=True)
    minutes          = Column(Integer)
    study_on         = Column(Date)
    studying_book_id = Column(Integer, ForeignKey("studying_books.id", ondelete='SET NULL'))
    created_at       = Column(DateTime, default=func.now())
    updated_at       = Column(DateTime, default=func.now(), onupdate=func.now())



