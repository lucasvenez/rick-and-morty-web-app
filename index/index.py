from datetime import datetime

from flask import Blueprint, render_template

index_blueprint = Blueprint("index_blueprint", __name__)


@index_blueprint.route("/", methods=["GET"])
@index_blueprint.route("/index", methods=["GET"])
def index():

    current_timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    return render_template("index.html", now=current_timestamp)
