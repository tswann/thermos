from thermos import app, db
from thermos.models import User, Bookmark, Tag
from flask.ext.script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def insert_data():
    tam = User(username='tam', email='tam@example.com', password='test')
    db.session.add(tam)

    def add_bookmark(url, description, tags):
        db.session.add(Bookmark(url=url, description=description, user=tam, tags=tags))

    for name in ["python", "flask", "webdev", "programming", "training", "news", "orm", "databases", "emacs", "gtd", "django"]:
        db.session.add(Tag(name=name))
    db.session.commit()

    add_bookmark("http://www.pluralsight.com", "Pluralsight. Hardcore developer training.", "training,programming,python,flask,webdev")
    add_bookmark("http://werkzeug.pocoo.org", "Werkzeug. The tool behind flask.", "programming,webdev,python,flask")

    db.session.commit()


@manager.command
def dropdb():
    if prompt_bool('Are you sure you want to lose all your data?'):
        db.drop_all()
        print 'Dropped the database'

if __name__ == '__main__':
    manager.run()
