from flask import Flask
from index import index_blueprint


def main():
    application = Flask(__name__)

    application.config.from_object("config.DevelopmentConfig")

    application.register_blueprint(index_blueprint)

    application.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
