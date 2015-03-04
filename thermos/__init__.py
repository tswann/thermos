import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xaa\x1d\xa8\xe5\xe5\xac!m\x1b\xf30P\x03Z\x8d.\x94\xa7P\x07\xc8G\x152'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['DEBUG'] = None
db = SQLAlchemy(app)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

import models
import views
