from flask_login import UserMixin

from main import db


class User(UserMixin):
    name: str = None
    email: str = None
    password: str = None
    birthdate: str = None

    def __init__(self, name, email, password, birthdate):
        self.name = name
        self.email = email
        self.password = password
        self.birthdate = birthdate

    def get_id(self):
        return self.email


class Character(db.Model):
    __tablename__ = "character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    created = db.Column(db.String(15), nullable=False)
    gender = db.Column(db.String(5), nullable=True)
    status = db.Column(db.String(5), nullable=True)
    species = db.Column(db.String(20), nullable=True)
