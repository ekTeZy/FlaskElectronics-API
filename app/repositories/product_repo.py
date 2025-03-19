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
    def get_product_by_id(product_id: int) -> Product:

        product: Optional[Product] = db.session.query(
            Product).filter_by(id=product_id).first()

        return product

    @staticmethod
    def get_product_by_name(name: str) -> Optional[Product]:
        return db.session.query(Product).filter_by(name=name).first()

    @staticmethod
    def create_product(name: str, category_id: int) -> Product:
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
    def update_product_by_id(product_id: int, updated_data: dict[str, str | int]) -> Optional[Product]:
        product = db.session.query(Product).filter_by(id=product_id).first()

        if not product:
            return None

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
    def delete_product(product: Product) -> None:

        try:
            db.session.delete(product)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise InternalServerError(
                f"Ошибка при удалении продукта: {str(e)}")
