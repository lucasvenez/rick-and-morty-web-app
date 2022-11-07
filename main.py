from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    import datetime

    application = Flask(__name__)
    application.config.from_object(
        "config.DevelopmentConfig")

    db.init_app(application)

    from index.routes import index_blueprint
    application.register_blueprint(index_blueprint)

    from character.routes import character_blueprint
    application.register_blueprint(character_blueprint)

    from login.routes import login_blueprint
    application.register_blueprint(login_blueprint)

    from login import login_manager
    login_manager.init_app(application)

    if application.config["TESTING"]:
        with application.app_context():
            db.drop_all()
            db.create_all()

            from util.crawler import get_data_from_rick_and_morty_apis
            get_data_from_rick_and_morty_apis(db)

            db.session.add(User(
                name="Lucas Venezian Povoa",
                email="lucasvenez@gmail.com",
                password="123456",
                birthdate=datetime.date(year=1990, month=2, day=1)
            ))
            db.session.commit()

    return application

from model import *

if __name__ == "__main__":
    application = create_app()
    print(application.url_map)
    application.run(host="0.0.0.0", port=5000)
