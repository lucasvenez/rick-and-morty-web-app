from flask import Blueprint
from .routes import *

character_blueprint = Blueprint(
    "character_blueprint", __name__, url_prefix="/character")
