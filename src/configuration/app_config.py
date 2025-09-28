from datetime import timedelta

from flask import Flask

from configuration.extensions import cors, jwt
from routers.url_router import urls_bp
from routers.user_router import user_bp
from src.configuration.config import Config
from src.database.db import connect_db


def add_configuration(app: Flask):
    app.config['JWT_SECRET_KEY'] = Config.JWT_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=60)
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']


def add_blueprints(app: Flask):
    app.register_blueprint(user_bp)
    app.register_blueprint(urls_bp)


def add_extensions(app: Flask):
    cors.init_app(app, origins=["http://127.0.0.1:5500"], supports_credentials=True)
    jwt.init_app(app)


def create_app(name):
    app = Flask(name)
    connect_db()
    add_configuration(app)
    add_blueprints(app)
    add_extensions(app)
    return app


