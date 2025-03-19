from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()


def init_db(app: Flask) -> None:
    app.config.from_object(Config)

    from app.models import category, product, sale

    db.init_app(app)
    migrate.init_app(app, db)
