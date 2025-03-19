from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from app.services.product_service import ProductService

products_bp = Blueprint("products", __name__, url_prefix="/products")


@products_bp.route("/", methods=["GET"])
def get_all_products():
    products = ProductService.get_all_products()

    return jsonify(products), 200


@products_bp.route("/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id: int):
    try:
        product = ProductService.get_product_by_id(product_id)

        return jsonify(product), 200

    except NotFound as e:
        return jsonify({"error": str(e)}), 404


@products_bp.route("/", methods=["POST"])
def create_product():
    try:
        data = request.get_json()
        new_product = ProductService.create_product(data)

        return jsonify(new_product), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

    except InternalServerError as e:
        return jsonify({"error": str(e)}), 500


@products_bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id: int):
    try:
        data = request.get_json()
        updated_product = ProductService.update_product_by_id(product_id, data)

        return jsonify(updated_product), 200

    except NotFound as e:
        return jsonify({"error": str(e)}), 404

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

    except InternalServerError as e:
        return jsonify({"error": str(e)}), 500


@products_bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id: int):
    try:
        response = ProductService.delete_product_by_id(product_id)

        return jsonify(response), 200

    except NotFound as e:
        return jsonify({"error": str(e)}), 404

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400

    except InternalServerError as e:
        return jsonify({"error": str(e)}), 500
