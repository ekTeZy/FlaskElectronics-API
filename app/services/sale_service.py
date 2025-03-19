from typing import List
from app.repositories.sale_repo import SaleRepository
from app.utils.cache import CacheManager
from werkzeug.exceptions import (
    BadRequest
)
import logging
import time
from datetime import datetime

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


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
        cache_key = f"total_sales:{start_date}:{end_date}"
        cached_data = CacheManager.get(cache_key)

        if cached_data is not None:
            logging.info(
                f"[CACHE] get_total_sales({start_date}, {end_date}) → КЭШ, total_sales={cached_data}")
            return cached_data

        start_time = time.time()

        start_date_dt = SaleService.parse_date(start_date)
        end_date_dt = SaleService.parse_date(end_date)

        total_sales = SaleRepository.get_total_sales(
            start_date_dt, end_date_dt)
        CacheManager.set(cache_key, total_sales)

        execution_time = time.time() - start_time

        logging.info(f"[DB] get_total_sales({start_date}, {end_date}) → БД "
                     f"time={execution_time:.4f} сек.")

        return total_sales

    @staticmethod
    def get_top_selling_products(start_date: str, end_date: str, limit: int) -> List[dict]:
        cache_key = f"top_products:{start_date}:{end_date}:{limit}"
        cached_data = CacheManager.get(cache_key)

        if cached_data is not None:
            logging.info(
                f"[CACHE] get_top_selling_products({start_date}, {end_date}, {limit}) → КЭШ")
            return cached_data

        start_time = time.time()

        start_date_dt = SaleService.parse_date(start_date)
        end_date_dt = SaleService.parse_date(end_date)

        top_selling_products = SaleRepository.get_top_selling_products(
            start_date_dt, end_date_dt, limit
        )

        CacheManager.set(cache_key, top_selling_products)

        execution_time = time.time() - start_time
        logging.info(f"[DB] get_top_selling_products({start_date}, {end_date}, {limit}) → БД "
                     f"time={execution_time:.4f} сек.")

        return top_selling_products
