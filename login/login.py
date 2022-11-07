from flask_login import LoginManager

from model import User

login_manager = LoginManager()


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
