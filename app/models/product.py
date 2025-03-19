from app.database import db


class Product(db.Model):
    __tablename__: str = "products"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(255), nullable=False)
    category_id: int = db.Column(
        db.Integer, db.ForeignKey("categories.id"), nullable=False)
