from flask import Blueprint

login_blueprint = Blueprint("login_blueprint", __name__)

from .routes import *
