import os


class Config(object):
    TESTING = False
    DEBUG = False


class ProductionConfig(Config):
    DATABASE_URI = os.getenv("DATABASE_URI")


class DevelopmentConfig(Config):
    DATABASE_URI = "sql:///:memory:"
    TESTING = True
    DEBUG = True

