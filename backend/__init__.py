from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from backend.config import Config


db = SQLAlchemy()
#bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__, static_folder = "../frontend/dist",
            template_folder = "../frontend/dist")
    app.config.from_object(Config)

    db.init_app(app)
    #bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    @app.route('/')
    def index():
        return render_template("index.html")
    """
    from backend.users.routes import users
    from backend.posts.routes import posts
    from backend.main.routes import main
    from backend.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    """

    return app
