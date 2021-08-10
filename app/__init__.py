# app/__init__

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap

from flask_login import LoginManager    # LoginManager is a class to manage user login and session
from flask_bcrypt import Bcrypt         # for password hashing

db = SQLAlchemy()

bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'    # let the log in manager know this is our log in system do_the_login() function in auto.route
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()

@login_manager.user_loader  # add this on login_manager exception
def create_app(config_type):    # config_type -> may be dev, test or prod
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')

    # eg configuration = '/home/ttpl8/pydev/book_catalog/config/dev.py'

    app.config.from_pyfile(configuration)

    db.init_app(app)    # bind database to flask app

    bootstrap.init_app(app)     # initializing bootstrap

    login_manager.init_app(app)     # initializing login manager

    bcrypt.init_app(app)    # initialize flask_bcrypt

    #   import app/catalog  Blueprint variable -> this time app is folder name not flask instance
    from app.catalog import main    # import blueprint
    app.register_blueprint(main)    # register blueprint

    # import from auth
    from app.auth import authentication
    app.register_blueprint(authentication)

    return app



