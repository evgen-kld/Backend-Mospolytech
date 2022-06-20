from flask import Flask, render_template

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

@app.route('/')
def index():
    return render_template('index.html')