from typing import Optional, List
from app.database import db
from app.models.category import Category
from werkzeug.exceptions import NotFound, BadRequest


class CategoryRepository:

    @staticmethod
    def category_exists_by_id(category_id: int) -> bool:
        return db.session.query(Category.id).filter_by(id=category_id).scalar() is not None
