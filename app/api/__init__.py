from flask import Blueprint
from app.api.products import products_bp

bp_api = Blueprint("api", __name__, url_prefix="/api")

bp_api.register_blueprint(products_bp)