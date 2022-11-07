import os


class Config(object):
    TESTING = False
    DEBUG = False


class ProductionConfig(Config):
    DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI


class DevelopmentConfig(Config):

    SECRET_KEY = "MY-SUPER-SECRET-KEY"

    TESTING = DEBUG = True

    DATABASE_URI = "sqlite:///:memory:"

    SQLALCHEMY_DATABASE_URI = DATABASE_URI

    SESSION_PROTECTION = "strong"

