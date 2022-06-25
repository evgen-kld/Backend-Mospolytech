from models import Book, Cover, Book_Genre
import hashlib
import uuid
import os
from werkzeug.utils import secure_filename
from app import db, app


class BooksFilter:
    def __init__(self):
        self.query = Book.query
        self.qwerty = Book_Genre.query

    def perform(self, title='', genres_list='', years_list='', amount_from='', amount_to='', author=''):
        if title != '':
            self.query = self.query.filter(Book.title.ilike(f'%{title}%'))
        if genres_list != []:
            self.qwerty =  self.qwerty.filter(Book_Genre.genres_id.in_(genres_list))
            self.query = self.query.join(self.qwerty)
        if years_list != []:
            years_list = [int(x) for x in years_list]
            self.query = self.query.filter(Book.year.in_(years_list))
        if amount_from != '':
            self.query = self.query.filter(Book.amount >= int(amount_from))
        if amount_to != '':
            self.query = self.query.filter(Book.amount <= int(amount_to))
        if author != '':
            self.query = self.query.filter(Book.author.ilike(f'%{author}%'))
        print(self.query)
        return self.query.order_by(Book.year.desc())



class ImageSaver:
    def __init__(self, file):
        self.file = file

    def save(self, book_id):
        self.img = self.__find_by_md5_hash()
        if self.img is not None:
            return self.img
        file_name = secure_filename(self.file.filename)
        self.img = Cover(
            id=str(uuid.uuid4()),
            file_name=file_name,
            mime_type=self.file.mimetype,
            md5_hash=self.md5_hash,
            book_id=book_id)
        self.file.save(
            os.path.join(app.config['UPLOAD_FOLDER'],
                         self.img.storage_filename))
        db.session.add(self.img)
        db.session.commit()
        return self.img

    def __find_by_md5_hash(self):
        self.md5_hash = hashlib.md5(self.file.read()).hexdigest()
        self.file.seek(0)
        return Cover.query.filter(Cover.md5_hash == self.md5_hash).first()