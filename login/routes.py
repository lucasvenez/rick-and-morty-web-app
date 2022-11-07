from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError

from main import db
from . import login_blueprint
from .forms import LoginForm, RegisterForm
from model import User


@login_blueprint.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        email = str(login_form.email.data)
        user = User.query.filter_by(email=email).first()
        if user is not None:
            if user.verify_password(login_form.password.data):
                login_user(user)
                return redirect(url_for("index_blueprint.index"))

        return "Usuário ou senha inválidos", 200

    return render_template("login/login.html", form=login_form)


@login_blueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("index_blueprint.index"))


@login_blueprint.route("/register", methods=["GET", "POST"])
def register():

    register_form = RegisterForm()

    if register_form.validate_on_submit():

        try:

            user = User(
                name=register_form.name.data,
                email=register_form.email.data,
                password=register_form.password.data,
                birthdate=register_form.birthdate.data)

            db.session.add(user)

            db.session.commit()

            return "Cadastro realizado com sucesso", 200

        except IntegrityError:
            db.session.rollback()
            return "E-mail já existente", 200

        except Exception as e:
            print(str(e))

    return render_template("login/register.html", form=register_form)
