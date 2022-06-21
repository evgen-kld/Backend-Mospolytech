from flask import Blueprint, redirect, render_template, request, url_for, flash
from app import db

bp = Blueprint('book', __name__, url_prefix='/book')

from models import Genre, Book, Book_Genre
from tools import ImageSaver


@bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        genres = Genre.query.all()
        return render_template('book/new.html', genres=genres)
    if request.method == 'POST':


        title = request.form.get('title')
        author = request.form.get('author')
        publisher = request.form.get('publisher')
        amount = request.form.get('amount')
        year = request.form.get('year')
        description = request.form.get('description')
        book = Book(title=title, description=description, year=year, publisher=publisher, author=author, amount=amount)
        db.session.add(book)
        db.session.commit()
        f = request.files.get('cover_img')
        if f and f.filename:
            cover = ImageSaver(f).save(book.id)
        genres = request.form.getlist('genre_id')
        for i in genres:
            genre_in_db = Book_Genre(books_id=book.id, genres_id=i)
            db.session.add(genre_in_db)
            db.session.commit()
        flash(f'Книга "{book.title}" успешно добавлена!', 'success')
        return redirect(url_for('index'))
        


        
