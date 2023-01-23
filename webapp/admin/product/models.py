from sqlalchemy.orm import relationship

from webapp.models import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    calories = db.Column(db.String)

    def __repr__(self) -> str:
        return (
            f"Product id: {self.id}, title: {self.title}, price: {self.price}, "
            f"description: {self.description}, calories: {self.calories}"
         )