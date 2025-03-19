from flask import Flask
from app.config import Config
from app.api import bp_api
from app.database import db, init_db


def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    app.config["JSON_AS_ASCII"] = False

    app.register_blueprint(bp_api)

    return app
