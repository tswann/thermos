from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xaa\x1d\xa8\xe5\xe5\xac!m\x1b\xf30P\x03Z\x8d.\x94\xa7P\x07\xc8G\x152'

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}, {}.".format(self.firstname[0], self.lastname[0])

bookmarks = []

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title="Title passed from view to template",
                           user=User("Tom", "Swann"))

def store_bookmark(url):
    bookmarks.append(dict(
                     url = url,
                     user = "tom",
                     date = datetime.utcnow()
                     ))

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash("Stored bookmark: '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
