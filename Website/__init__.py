from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

DB_NAME = "database.db"


def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "CE205 Team Project"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    # init database
    db.init_app(app)

    from .view import views
    from .auth import auth

    app.register_blueprint(views , url_prefix = "/")
    app.register_blueprint(auth , url_prefix = "/")

    from .models import  User , Note

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()

    login_manager.login_view= "auth.login"

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app