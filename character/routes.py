from flask import Blueprint, render_template

from character import character_blueprint
from model import Character


@character_blueprint.route("/", methods=["GET"])
def list_characters():
    return render_template(
        template_name_or_list="character/list.html",
        characters=Character.query.all())
