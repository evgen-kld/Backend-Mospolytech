from app import db
import sqlalchemy as sa
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import os
from flask import url_for


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), nullable=False, unique=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    middle_name = db.Column(db.String(20))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<User: %r>' % self.login

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))

    def __repr__(self):
        return '<User: %r>' % self.role_name




books_genres = db.Table('books_genres',
    db.Column('books_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('genres_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    short_description = db.Column(db.Text)
    year = db.Column(db.Date, nullable=False)
    publisher = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    rating_sum = db.Column(db.Integer, nullable=False, default=0)
    rating_num = db.Column(db.Integer, nullable=False, default=0)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Book: %r>' % self.title

    @property
    def rating(self):
        if self.rating_num > 0:
            return self.rating_sum / self.rating_num
        return 0

    genres = db.relationship('Genre', secondary=books_genres, lazy='subquery', backref=db.backref('books', lazy=True))
    reviews = db.relationship('Review')


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return '<Genre: %r>' % self.genre_name

class Cover(db.Model):
    __tablename__ = 'covers'
    id = db.Column(db.String(100), primary_key=True)
    file_name = db.Column(db.String(100), nullable=False)
    mime_type = db.Column(db.String(100), nullable=False)
    md5_hash = db.Column(db.String(100), nullable=False, unique=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), unique=True)

    def __repr__(self):
        return '<Cover: %r>' % self.file_name

    @property
    def storage_filename(self):
        _, ext = os.path.splitext(self.file_name)
        return self.id + ext

    @property
    def url(self):
        return url_for('image', image_id=self.id)


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    rating = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=sa.sql.func.now())

    def __repr__(self):
        return f'<Reviews: {self.user_id} {self.created_at}>'

