from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from app.services.sale_service import SaleService

sales_bp = Blueprint("products", __name__, url_prefix="/sales")