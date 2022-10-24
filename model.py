from main import db
from datetime import datetime


class Character(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), nullable=False)

    created = db.Column(db.String(15), nullable=False,
                        default=str(datetime.utcnow()))

    gender = db.Column(db.String(5), nullable=True)

    status = db.Column(db.String(5), nullable=True)

    species = db.Column(db.String(20), nullable=True)
