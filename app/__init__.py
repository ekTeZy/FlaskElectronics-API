from flask import Flask
from app.config import Config
from app.database import db, init_db

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)
    return app
