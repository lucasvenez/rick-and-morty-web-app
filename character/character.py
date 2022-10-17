from flask import Blueprint, render_template
from model import Character

character_blueprint = Blueprint(
    "character_blueprint", __name__,
    url_prefix="/character")


@character_blueprint.route("/", methods=["GET"])
def list_characters():
    characters = Character.query.all()
    for c in characters:
        print(c)
    return render_template(
        "character/list.html", characters=characters)
