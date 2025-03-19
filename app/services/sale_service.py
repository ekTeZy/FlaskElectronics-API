from app.repositories.sale_repo import SaleRepository
from werkzeug.exceptions import (
    BadRequest,
    NotFound,
)
from datetime import datetime


class SaleService:
    @staticmethod
    def get_all_sales() -> list[dict]:
        sales = SaleRepository.get_all_sales()
        return [s.to_dict() for s in sales]

    @staticmethod
    def get_total_sales(start_date: str, end_date: str) -> float:
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        
        except ValueError:
            raise BadRequest("Некорректные даты фильтра")

        total_sales = SaleRepository.get_total_sales(start_date, end_date)
        
        return total_sales

    @staticmethod
    def get_top_selling_products(start_date: str, end_date: str, limit: int) -> list[dict]:
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            limit = int(limit)
            if limit <= 0:
                raise ValueError("Лимит должен быть положительным числом")
        
        except ValueError:
            raise BadRequest("Некорректные даты фильтра или лимит")
        
        top_selling_products = SaleRepository.get_top_selling_products(
            start_date, end_date, limit)
        
        return top_selling_products