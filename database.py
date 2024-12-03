from email.policy import default
from xmlrpc.client import boolean

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship

db = SQLAlchemy()
class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    name_book = db.Column(db.String, nullable=True)
    added = db.Column(db.DateTime, nullable=False, default=func.now())
    is_read = db.Column(db.Boolean, default=False)

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id", ondelete="SET NULL"))
    genre = relationship("Genre", back_populates="book")
    def __repr__(self):
        return f"User(name_book={self.name_book!r})"

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String, nullable=True)

    book = relationship("Book", back_populates="genre")

    def __repr__(self):
        return f"{self.genre!r}"

