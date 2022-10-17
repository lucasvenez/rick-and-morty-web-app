from flask import Blueprint

index_blueprint = Blueprint("index", __name__)


@index_blueprint.route("/", methods=["GET"])
@index_blueprint.route("/index", methods=["GET"])
def index():
    return "Olá, Mundo! Como vai?"
