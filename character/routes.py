from flask import render_template
from flask_login import login_required

from character import character_blueprint
from character.forms import CharacterForm
from main import db

from model import Character


@character_blueprint.route("/", methods=["GET"])
@login_required
def list_characters():
    return render_template(
        template_name_or_list="character/list.html",
        characters=Character.query.all())


@character_blueprint.route("/new", methods=["GET", "POST"])
def new_character():
    form = CharacterForm()

    if form.validate_on_submit():
        character = Character(id=int(form.id.data), name=str(form.name.data))
        db.session.add(character)
        db.session.commit()
        return "Personagem inserido com sucesso", 200

    return render_template("character/new.html", form=form)
