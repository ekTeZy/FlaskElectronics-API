from flask import Blueprint
from app.api.products import products_bp
from app.api.sales import sales_bp

bp_api = Blueprint("api", __name__, url_prefix="/api")

bp_api.register_blueprint(products_bp)
bp_api.register_blueprint(sales_bp)