from flask import render_template, redirect, url_for
from flask_login import login_user

from . import login_blueprint
from .forms import LoginForm
from model import users


@login_blueprint.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        email = str(login_form.email.data)
        user = users.get(email)
        if user is not None:
            if user.password == login_form.password.data:
                login_user(user)
                return redirect(url_for("index_blueprint.index"))

        return "Usuário ou senha inválidos", 200

    return render_template("login/login.html", form=login_form)
