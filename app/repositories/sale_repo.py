from typing import List
from app.database import db
from app.models.sale import Sale
from app.models.product import Product
from datetime import datetime
from sqlalchemy import func


class SaleRepository:

    @staticmethod
    def get_all_sales() -> List[Sale]:
        return db.session.query(Sale).all()

    @staticmethod
    def get_total_sales(start_date: datetime, end_date: datetime) -> float:
        total_sales = db.session.query(func.coalesce(func.sum(Sale.quantity), 0.0)).filter(
            Sale.date.between(start_date, end_date)).scalar()

        return total_sales

    @staticmethod
    def get_top_selling_products(start_date: datetime, end_date: datetime, limit: int) -> List[dict]:
        top_selling_products = (
            db.session.query(Product.name, func.sum(
                Sale.quantity).label("total_quantity"))
            .join(Sale, Product.id == Sale.product_id)
            .filter(Sale.date.between(start_date, end_date))
            .group_by(Product.name)
            .order_by(func.sum(Sale.quantity).desc())
            .limit(limit)
            .all()
        )

        return [{"product": product[0], "total_quantity": product[1]} for product in top_selling_products]
