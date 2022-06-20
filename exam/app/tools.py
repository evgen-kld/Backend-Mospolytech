from models import Book
from app import db, app

class BooksFilter:
    def __init__(self):
        self.query = Book.query

    def perform(self):
        return self.query.order_by(Book.year.desc())