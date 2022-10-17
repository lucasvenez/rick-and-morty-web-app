from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config.from_object("config.DevelopmentConfig")

database = SQLAlchemy()
database.init_app(application)


from index import index_blueprint
from character import character_blueprint

def main():
    # from util.crawler import get_data_from_rick_and_morty_apis

    if application.config["TESTING"]:
        with application.app_context():
            database.drop_all()
            database.create_all()
            # get_data_from_rick_and_morty_apis(database)

    application.register_blueprint(index_blueprint)
    application.register_blueprint(character_blueprint)

    application.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
