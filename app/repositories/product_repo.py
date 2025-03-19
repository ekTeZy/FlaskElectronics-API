from typing import Optional, List
from app.database import db
from app.models.product import Product
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError
from app.repositories.categoty_repo import CategoryRepository


class ProductRepository:

    @staticmethod
    def get_all_products() -> List[Product]:
        return db.session.query(Product).all()

    @staticmethod
    def get_product_by_id(product_id: int) -> Optional[Product]:
        if product_id <= 0:
            raise BadRequest(
                f"Некорректный идентификатор продукта: {product_id}")

        product = db.session.query(Product).where(
            Product.id == product_id).first()

        if product is None:
            raise NotFound(f"Продукт с id {product_id} не найден")

        return product

    @staticmethod
    def get_product_by_name(name: str) -> Optional[Product]:
        product = db.session.query(Product).where(
            Product.name == name).first()

        return product if product is not None else None

    @staticmethod
    def create_product(data: dict) -> Product:
        name = data.get("name")
        category_id = data.get("category_id")

        if not isinstance(name, str) or not isinstance(category_id, int):
            raise BadRequest(f"Имя и id категории обязательные поля")

        if not CategoryRepository.category_exists_by_id(category_id=category_id):
            raise BadRequest(f"Такого id категории не существует")

        existing_product = ProductRepository.get_product_by_name(name=name)

        if existing_product:
            raise BadRequest("Продукт с таким именем уже существует")

        new_product: Product = Product(
            name=name,
            category_id=category_id
        )
        try:
            db.session.add(new_product)
            db.session.commit()
            return new_product

        except Exception as e:
            db.session.rollback()
            raise InternalServerError(
                f"Ошибка при создании продукта: {str(e)}")
