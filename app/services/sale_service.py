from typing import List
from app.repositories.sale_repo import SaleRepository
from werkzeug.exceptions import (
    BadRequest
)
from datetime import datetime


class SaleService:
    @staticmethod
    def get_all_sales() -> list[dict]:
        sales = SaleRepository.get_all_sales()
        return [s.to_dict() for s in sales]

    @staticmethod
    def parse_date(date_str: str) -> datetime:
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")

        except ValueError:
            raise BadRequest(
                f"Некорректный формат даты: {date_str}. Используйте YYYY-MM-DD.")

    @staticmethod
    def get_total_sales(start_date: str, end_date: str) -> float:
        start_date_dt = SaleService.parse_date(start_date)
        end_date_dt = SaleService.parse_date(end_date)

        return SaleRepository.get_total_sales(start_date_dt, end_date_dt)

    @staticmethod
    def get_top_selling_products(start_date: str, end_date: str, limit: int) -> List[dict]:
        start_date_dt = SaleService.parse_date(start_date)
        end_date_dt = SaleService.parse_date(end_date)

        if not isinstance(limit, int) or limit <= 0:
            raise BadRequest("Лимит должен быть положительным целым числом.")

        return SaleRepository.get_top_selling_products(start_date_dt, end_date_dt, limit)
