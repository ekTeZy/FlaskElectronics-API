from typing import List
from app.database import db
from app.models.sale import Sale
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
