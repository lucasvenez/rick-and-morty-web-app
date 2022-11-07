from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = EmailField("E-mail", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Logar")


class RegisterForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired()])
    email = EmailField("E-mail", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[
        DataRequired(),
        EqualTo("confirm", message="Senhas devem ser compactíveis")])
    confirm = PasswordField("Confirmação")
    birthdate = StringField("Data de aniversário", validators=[DataRequired()])
    submit = SubmitField("Cadastrar")
