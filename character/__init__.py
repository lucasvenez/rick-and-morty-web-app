from flask import Blueprint

character_blueprint = Blueprint(
    "character_blueprint", __name__, url_prefix="/character")

from .routes import *
