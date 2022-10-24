from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from model import *

db = SQLAlchemy()
login_manager = LoginManager()


@login_manager.user_loader
def user_loader(user_id):
    from model import users
    return users.get(user_id)


def create_app():
    application = Flask(__name__)
    application.config.from_object(
        "config.DevelopmentConfig")

    from index.routes import index_blueprint
    application.register_blueprint(index_blueprint)

    from character.routes import character_blueprint
    application.register_blueprint(character_blueprint)

    from login.routes import login_blueprint
    application.register_blueprint(login_blueprint)

    db.init_app(application)
    login_manager.init_app(application)

    if application.config["TESTING"]:
        with application.app_context():
            db.drop_all()
            db.create_all()
            from util.crawler import get_data_from_rick_and_morty_apis
            get_data_from_rick_and_morty_apis(db)

    return application


if __name__ == "__main__":
    application = create_app()
    print(application.url_map)
    application.run(host="0.0.0.0", port=5000)
