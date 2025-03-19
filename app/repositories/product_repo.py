from typing import Optional, List
from app.database import db
from app.models.product import Product
from werkzeug.exceptions import (
    NotFound,
    BadRequest,
    InternalServerError
)
from app.repositories.category_repo import CategoryRepository


class ProductRepository:

    @staticmethod
    def get_all_products() -> List[Product]:
        return db.session.query(Product).all()

    @staticmethod
    def get_product_by_id(product_id: int) -> Optional[Product]:
        if product_id <= 0:
            raise BadRequest(
                f"Некорректный идентификатор продукта: {product_id}")

        product: Optional[Product] = db.session.query(
            Product).filter_by(id=product_id).first()

        if product is None:
            raise NotFound(f"Продукт с id {product_id} не найден")

        return product

    @staticmethod
    def get_product_by_name(name: str) -> Optional[Product]:
        return db.session.query(Product).filter_by(name=name).first()

    @staticmethod
    def create_product(data: dict[str, str | int]) -> Product:
        name: Optional[str] = data.get("name")
        category_id: Optional[int] = data.get("category_id")

        if not isinstance(name, str) or not isinstance(category_id, int):
            raise BadRequest("Имя и id категории обязательные поля")

        if not CategoryRepository.category_exists_by_id(category_id):
            raise BadRequest("Такого id категории не существует")

        existing_product: Optional[Product] = ProductRepository.get_product_by_name(
            name)

        if existing_product:
            raise BadRequest("Продукт с таким именем уже существует")

        new_product = Product(name=name, category_id=category_id)

        try:
            db.session.add(new_product)
            db.session.commit()
            return new_product

        except Exception as e:
            db.session.rollback()
            raise InternalServerError(
                f"Ошибка при создании продукта: {str(e)}")

    @staticmethod
    def update_product_by_id(product_id: int, updated_data: dict[str, str | int]) -> Product:
        """Обновить продукт по ID"""
        product: Optional[Product] = db.session.query(
            Product).filter_by(id=product_id).first()

        if "category_id" in updated_data:
            if not CategoryRepository.category_exists_by_id(updated_data["category_id"]):
                raise BadRequest("Категория с таким ID не существует")

        if not product:
            raise NotFound(f"Продукт с id {product_id} не найден")

        for key, value in updated_data.items():
            if hasattr(product, key):
                setattr(product, key, value)

        try:
            db.session.commit()
            db.session.refresh(product)
            return product

        except Exception as e:
            db.session.rollback()
            raise InternalServerError(
                f"Ошибка при обновлении продукта: {str(e)}")

    @staticmethod
    def delete_product_by_id(product_id: int) -> bool:
        """Удалить продукт по ID"""
        existing_product: Optional[Product] = ProductRepository.get_product_by_id(
            product_id)

        if not existing_product:
            raise BadRequest("Продукта с таким id не существует")

        try:
            db.session.delete(existing_product)
            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
            raise InternalServerError(
                f"Ошибка при удалении продукта: {str(e)}")
