from flask import Flask


def main():
    application = Flask(__name__)

    application.config.from_object("config.DevelopmentConfig")


    application.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
