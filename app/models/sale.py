from app.database import db


class Sale(db.Model):
    __tablename__: str = "sales"

    id: int = db.Column(db.Integer, primary_key=True)
    product_id: int = db.Column(
        db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
