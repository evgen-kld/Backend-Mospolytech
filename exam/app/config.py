import os

SECRET_KEY = '123456qwerty'
SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://std_1760_exam:11111111@std-mysql.ist.mospolytech.ru/std_1760_exam'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')