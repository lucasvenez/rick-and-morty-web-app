from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField, DateField
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
        EqualTo("confirm", message="Senhas devem ser compatíveis")])
    confirm = PasswordField("Confirmação")
    birthdate = DateField("Data de aniversário", validators=[DataRequired()], format=["%d/%m/%Y", "%Y-%m-%d"])
    submit = SubmitField("Cadastrar")
