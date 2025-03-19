from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from app.services.sale_service import SaleService

sales_bp = Blueprint("products", __name__, url_prefix="/sales")

@sales_bp.route("/total", methods=["GET"])
def get_total_sales():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    
    if not start_date or not end_date:
        raise BadRequest("Необходимо указать даты начала и конца периода")
    
    try:
        total_sales = SaleService.get_total_sales(start_date, end_date)

        return jsonify({"total_sales": total_sales}), 200
    
    except NotFound as e:
        return jsonify({"error": str(e)}), 404