from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from app.services.sale_service import SaleService

sales_bp = Blueprint("sales", __name__, url_prefix="/sales")


@sales_bp.route("/total", methods=["GET"])
def get_total_sales():
    """Получить общую сумму продаж за период"""
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    if not start_date or not end_date:
        raise BadRequest(
            "Необходимо указать даты начала и конца периода (start_date, end_date)")

    try:
        total_sales = SaleService.get_total_sales(start_date, end_date)
        return jsonify({"total_sales": total_sales}), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

    except NotFound as e:
        return jsonify({"error": str(e)}), 404

    except InternalServerError as e:
        return jsonify({"error": f"Ошибка сервера: {str(e)}"}), 500


@sales_bp.route("/top-products", methods=["GET"])
def get_top_selling_products():
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    limit = request.args.get("limit")

    if not start_date or not end_date or not limit:
        raise BadRequest(
            "Необходимо указать даты начала и конца периода (start_date, end_date)")

    try:
        limit = int(limit)
        if limit <= 0:
            raise BadRequest("Лимит должен быть положительным целым числом.")

        top_selling_products = SaleService.get_top_selling_products(
            start_date, end_date, limit)
        
        return jsonify({"top_selling_products": top_selling_products}), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

    except ValueError:
        return jsonify({"error": "Лимит должен быть целым числом."}), 400

    except InternalServerError as e:
        return jsonify({"error": f"Ошибка сервера: {str(e)}"}), 500
