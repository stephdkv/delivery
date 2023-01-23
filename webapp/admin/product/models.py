from sqlalchemy.orm import relationship

from webapp.models import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.Integer)
    description = db.Column(db.Text)
    calories = db.Column(db.String)
    is_active = db.Column(db.Boolean)
    categories = relationship("Category", secondary="product_categories", backref='products')

    def __repr__(self) -> str:
        return (
            f"Product id: {self.id}, title: {self.title}, price: {self.price}, "
            f"description: {self.description}, calories: {self.calories}"
        )


class ProductCategory(db.Model):
    __tablename__ = "product_categories"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.ForeignKey("products.id"))
    category_id = db.Column(db.ForeignKey("categories.id"))
    category = relationship("Category", backref="product_product_category")
    product = relationship("Product", backref="category_product_category")

    def __repr__(self) -> str:
        return (
            f"ProductCategory id: {self.id}, product_id: {self.product_id}, category_id: {self.category_id}, "
            f"extra_data: {self.extra_data}"
        )
