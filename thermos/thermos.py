import os
from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import BookmarkForm

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xaa\x1d\xa8\xe5\xe5\xac!m\x1b\xf30P\x03Z\x8d.\x94\xa7P\x07\xc8G\x152'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

bookmarks = []

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))

def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]

def store_bookmark(url, description):
    bookmarks.append(dict(
                     url = url,
                     user = "tom",
                     description = description,
                     date = datetime.utcnow()
                     ))

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
