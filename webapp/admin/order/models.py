from sqlalchemy.orm import relationship

from webapp import Product
from webapp.models import db


class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    basket_id = db.Column(db.Integer, db.ForeignKey("baskets.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    is_active = db.Column(db.Boolean)
    date_time = db.Column(db.DateTime)
    comment = db.Column(db.Text)
    deliveries = relationship("Delivery")
    baskets = relationship("Basket")
    users = relationship("User")

    def __repr__(self) -> str:
        return f"Order id: {self.id}, basket_id: {self.basket_id}, user_id: {self.user_id}," \
               f"date_time:{self.date_time}, comment:{self.comment}"


class Basket(db.Model):
    __tablename__ = "baskets"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    is_ordered = db.Column(db.Boolean)
    total = db.Column(db.Float)
    is_active = db.Column(db.Boolean)
    orders = relationship("Order")
    users = relationship("User")

    def __repr__(self) -> str:
        return (
            f"Basket id: {self.id}, user_id: {self.user_id}, is_ordered: {self.is_ordered}, "
            f"total: {self.total}, quantity: {self.is_active}"
        )


class BasketProduct(db.Model):
    __tablename__ = "basket_products"
    id = db.Column(db.Integer, primary_key=True)
    basket_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    base_price = db.Column(db.Float)
    final_price = db.Column(db.Float)
    is_active = db.Column(db.Boolean)

    def __repr__(self) -> str:
        return (
            f"BasketProduct id: {self.id}, basket_id: {self.basket_id}, product_id: {self.product_id}, "
            f"quantity: {self.quantity}, base_price: {self.base_price}, final_price: {self.final_price}, "
            f"quantity: {self.is_active}"
        )
