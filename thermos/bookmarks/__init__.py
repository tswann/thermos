__author__ = 'thomassw'

from flask import Blueprint

bookmarks = Blueprint('bookmarks', __name__)

from . import views