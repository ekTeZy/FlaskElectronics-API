from typing import Optional
from app.repositories.product_repo import ProductRepository
from app.repositories.category_repo import CategoryRepository
from werkzeug.exceptions import (
    BadRequest,
    NotFound,
)


class ProductService:

    @staticmethod
    def get_all_products() -> list[dict]:
        products = ProductRepository.get_all()
        return [p.to_dict() for p in products]

    @staticmethod
    def get_product_by_id(product_id: int) -> dict:
        if product_id <= 0:
            raise BadRequest("Некорректный ID продукта")

        product = ProductRepository.get_product_by_id(product_id)

        if not product:
            raise NotFound(f"Продукт с id {product_id} не найден")

        return product.to_dict()

    @staticmethod
    def create_product(data: dict[str, str | int]) -> dict:
        name: Optional[str] = data.get("name")
        category_id: Optional[int] = data.get("category_id")

        if not isinstance(name, str) or not isinstance(category_id, int):
            raise BadRequest("Имя и id категории обязательные поля")

        if not CategoryRepository.category_exists_by_id(category_id):
            raise BadRequest("Такого id категории не существует")

        existing_product = ProductRepository.get_product_by_name(name)

        if existing_product:
            raise BadRequest("Продукт с таким именем уже существует")

        new_product = ProductRepository.create_product(
            name=name, category_id=category_id)

        return new_product.to_dict()

    @staticmethod
    def update_product_by_id(product_id: int, data: dict[str, str | int]) -> dict:

        if product_id <= 0:
            raise BadRequest("Некорректный ID продукта")

        existing_product = ProductRepository.get_product_by_id(product_id)

        if not existing_product:
            raise NotFound(f"Продукт с id {product_id} не найден")

        if "category_id" in data:
            if not CategoryRepository.category_exists_by_id(data["category_id"]):
                raise BadRequest("Категория с таким ID не существует")

        updated_product = ProductRepository.update_product_by_id(
            product_id, data)

        return updated_product.to_dict()
