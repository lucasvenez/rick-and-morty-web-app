from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired



class CharacterForm(FlaskForm):
    id = IntegerField("Identificador", validators=[DataRequired()])
    name = StringField("Nome do Personagem", validators=[DataRequired()])
    gender = StringField("Gênero")
    status = StringField("Status")
    species = StringField("Especie")

    
=======
"""
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(30), nullable=False)
created = db.Column(db.String(15), nullable=False)
gender = db.Column(db.String(5), nullable=True)
status = db.Column(db.String(5), nullable=True)
species = db.Column(db.String(20), nullable=True)
"""
