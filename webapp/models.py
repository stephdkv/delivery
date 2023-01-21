from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# class Address(db.Model):
#     __tablename__ = "addresses"
#     id = db.Column(db.Integer, primary_key=True)
#     city = db.Column(db.String(30))
#     street = db.Column(db.String)
#     house = db.Column(db.String)
#     apartment = db.Column(db.String)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     deliveries = relationship("Delivery")
#
#     def __repr__(self) -> str:
#         return (
#             f"Address id: {self.id}, city: {self.city}, street: {self.street}, "
#             f"house: {self.house}, apartment: {self.apartment}, user_id: {self.user_id}"
#         )
#
#
# class Product(db.Model):
#     __tablename__ = "products"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     price = db.Column(db.Integer)
#     description = db.Column(db.Text)
#     calories = db.Column(db.String)
#     baskets = relationship("BasketProduct", backref="product")
#     categories = relationship("Category", secondary="product_category")
#
#     def __repr__(self) -> str:
#         return (
#             f"Product id: {self.id}, title: {self.title}, price: {self.price}, "
#             f"description: {self.description}, calories: {self.calories}"
#         )
#
#
# class ProductCategory(db.Model):
#     __tablename__ = "product_categories"
#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.ForeignKey("products.id"))
#     category_id = db.Column(db.ForeignKey("categories.id"))
#     extra_data = db.Column(db.String(100))
#     category = relationship("Category", backref="product_product_category")
#     product = relationship("Product", backref="category_product_category")
#
#     def __repr__(self) -> str:
#         return (
#             f"ProductCategory id: {self.id}, product_id: {self.product_id}, category_id: {self.category_id}, "
#             f"extra_data: {self.extra_data}"
#         )
#
#
# class Category(db.Model):
#     __tablename__ = "categories"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#
#     def __repr__(self) -> str:
#         return f"Category id: {self.id}, title: {self.title}"
#
#
# class Basket(db.Model):
#     __tablename__ = "baskets"
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     is_ordered = db.Column(db.Integer)
#     total = db.Column(db.Float)
#     orders = relationship("Order")
#     products = relationship("BasketProduct", backref="basket")
#
#     def __repr__(self) -> str:
#         return (
#             f"Basket id: {self.id}, user_id: {self.user_id}, is_ordered: {self.is_ordered}, "
#             f"total: {self.total}"
#         )
#
#
# class BasketProduct(db.Model):
#     __tablename__ = "basket_products"
#     id = db.Column(db.Integer, primary_key=True)
#     basket_id = db.Column(db.Integer, db.ForeignKey("baskets.id"))
#     product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
#     quantity = db.Column(db.Integer)
#     base_price = db.Column(db.Float)
#     final_price = db.Column(db.Float)
#     extra_data = db.Column(db.String(100))
#
#     def __repr__(self) -> str:
#         return (
#             f"BasketProduct id: {self.id}, basket_id: {self.basket_id}, product_id: {self.product_id}, "
#             f"quantity: {self.quantity}, base_price: {self.base_price}, final_price: {self.final_price}, "
#             f"extra_data: {self.extra_data}"
#         )
#
#
# class Order(db.Model):
#     __tablename__ = "orders"
#     id = db.Column(db.Integer, primary_key=True)
#     basket_id = db.Column(db.Integer, db.ForeignKey("baskets.id"))
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     deliveries = relationship("Delivery")
#
#     def __repr__(self) -> str:
#         return f"Delivery id: {self.id}, basket_id: {self.basket_id}, user_id: {self.user_id}"
#
#
#
#
# class Employer(db.Model):
#     __tablename__ = "employees"
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String)
#     last_name = db.Column(db.String)
#     phone = db.Column(db.String(11))
#     email = db.Column(db.String(120), unique=True)
#     register_date = db.Column(db.Date)
#     position_id = db.Column(db.Integer, db.ForeignKey("positions.id"))
#
#     def __repr__(self) -> str:
#         return (
#             f"Employer id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, "
#             f"phone: {self.phone}, email: {self.email}, register_date: {self.register_date}, "
#             f"position_id: {self.position_id}"
#         )
#
#
# class Position(db.Model):
#     __tablename__ = "positions"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     employers = relationship("Employer")
#
#     def __repr__(self) -> str:
#         return f"ProductIngredient id: {self.id}, title: {self.title}"
#
#
# class ProductIngredient(db.Model):
#     __tablename__ = "product_ingredients"
#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
#     ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"))
#
#     def __repr__(self) -> str:
#         return f"ProductIngredient id: {self.id}, product_id: {self.product_id}, ingredient_id: {self.ingredient_id}"
#
#
# class Ingredient(db.Model):
#     __tablename__ = "ingredients"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     caloric_100g = db.Column(db.Integer, db.ForeignKey("ingredients.id"))
#
#     def __repr__(self) -> str:
#         return f"Ingredient id: {self.id}, title: {self.title}, calories in 100g: {self.caloric_100g}"
#
#
# class IngredientsShipment(db.Model):
#     __tablename__ = "ingredient_shipments"
#     id = db.Column(db.Integer, primary_key=True)
#     ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"))
#     quantity = db.Column(db.Float)
#     measure_id = db.Column(db.Integer, db.ForeignKey("measures.id"))
#     price = db.Column(db.Float)
#
#     def __repr__(self) -> str:
#         return (
#             f"IngredientsShipment id: {self.id}, ingredient_id: {self.ingredient_id}, quantity: {self.quantity}, "
#             f"measure_id: {self.measure_id}, price: {self.price}"
#         )
#
#
# class Measure(db.Model):
#     __tablename__ = "measures"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#
#     def __repr__(self) -> str:
#         return f"Measure id: {self.id}, title: {self.title}"
