from app.database import db


class Category(db.Model):
    __tablename__: str = "categories"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(255), nullable=False, unique=True)

    products = db.relationship("Product", backref="category", lazy=True)
