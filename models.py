from sqlalchemy import (Column, Integer, String, DECIMAL,
                        Date, ForeignKey, Boolean, Text, Float)
from sqlalchemy.orm import relationship
from data_base import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    birthday = Column(Date())
    phone = Column(String(11))
    email = Column(String(120), unique=True)
    register_day = Column(Date())
    addresses = relationship('Address')
    orders = relationship('Order')
    baskets = relationship('Basket')

    def __repr__(self):
        return f'Client {self.id}, {self.full_name}'


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    city = Column(String(30))
    street = Column(String())
    house = Column(String())
    apartment = Column(String())
    user_id = Column(Integer, ForeignKey('users.id'))
    deliveries = relationship('Delivery')

    def __repr__(self) -> str:
        return f'Address id: {self.id}, city: {self.city}, street: {self.street}, ' \
               f'house: {self.house}, apartment: {self.apartment}, user_id: {self.user_id}'


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String())
    price = Column(Integer())
    description = Column(Text())
    calories = Column(String())
    baskets = relationship('BasketProduct', backref='product')
    categories = relationship('Category', secondary='product_category')

    def __repr__(self) -> str:
        return f'Product id: {self.id}, title: {self.title}, price: {self.price}, ' \
               f'description: {self.description}, calories: {self.calories}'


class ProductCategory(Base):
    __tablename__ = 'product_categories'
    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    category_id = Column(ForeignKey('categories.id'))
    extra_data = Column(String(100))
    category = relationship('Category', backref='product_product_category')
    product = relationship('Product', backref='category_product_category')
    
    def __repr__(self) -> str:
        return f'ProductCategory id: {self.id}, product_id: {self.product_id}, category_id: {self.category_id}, ' \
               f'extra_data: {self.extra_data}'


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    title = Column(String())

    def __repr__(self) -> str:
        return f'Category id: {self.id}, title: {self.title}'


class Basket(Base):
    __tablename__ = 'baskets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    is_ordered = Column(Integer())
    total = Column(Float())
    orders = relationship('Order')
    products = relationship('Basket_product', backref='basket')

    def __repr__(self) -> str:
        return f'Basket id: {self.id}, user_id: {self.user_id}, is_ordered: {self.is_ordered}, ' \
               f'total: {self.total}'


class BasketProduct(Base):
    __tablename__ = 'basket_products'
    id = Column(Integer, primary_key=True)
    basket_id = Column(Integer, ForeignKey('baskets.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer())
    base_price = Column(Float())
    final_price = Column(Float())
    extra_data = Column(String(100))

    def __repr__(self) -> str:
        return f'BasketProduct id: {self.id}, basket_id: {self.basket_id}, product_id: {self.product_id}, ' \
               f'quantity: {self.quantity}, base_price: {self.base_price}, final_price: {self.final_price}, ' \
               f'extra_data: {self.extra_data}'


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    basket_id = Column(Integer, ForeignKey('baskets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    deliveries = relationship('Delivery')

    def __repr__(self) -> str:
        return f'Delivery id: {self.id}, basket_id: {self.basket_id}, user_id: {self.user_id}'


class Delivery(Base):
    __tablename__ = 'deliveries'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    done = Column(Boolean())
    address_id = Column(Integer, ForeignKey('addresses.id'))
    pickup_point_id = Column(Integer, ForeignKey('pickup_points.id'))

    def __repr__(self) -> str:
        return f'Delivery id: {self.id}, order_id: {self.order_id}, done: {self.done}, ' \
               f'address_id: {self.address_id}, pickup_point_id: {self.pickup_point_id}'


class PickupPoint(Base):
    __tablename__ = 'pickup_points'
    id = Column(Integer, primary_key=True)
    title = Column(String())
    city = Column(String())
    street = Column(String())
    house = Column(String())
    deliveries = relationship('Delivery')

    def __repr__(self) -> str:
        return f'PickupPoint id: {self.id}, title: {self.title}, city: {self.city}, ' \
               f'street: {self.street}, house: {self.house}'


class Employer(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    phone = Column(String(11))
    email = Column(String(120), unique=True)
    register_date = Column(Date())
    position_id = Column(Integer, ForeignKey('positions.id'))

    def __repr__(self) -> str:
        return f'Employer id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}, ' \
               f'phone: {self.phone}, email: {self.email}, register_date: {self.register_date}, ' \
               f'position_id: {self.position_id}'


class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    title = Column(String())
    employers = relationship('Employer')

    def __repr__(self) -> str:
        return f'ProductIngredient id: {self.id}, title: {self.title}'


class ProductIngredient(Base):
    __tablename__ = 'product_ingredients'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))

    def __repr__(self) -> str:
        return f'ProductIngredient id: {self.id}, product_id: {self.product_id}, ingredient_id: {self.ingredient_id}'


class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    title = Column(String())
    caloric_100g = Column(Integer, ForeignKey('ingredients.id'))

    def __repr__(self) -> str:
        return f'Ingredient id: {self.id}, title: {self.title}, calories in 100g: {self.caloric_100g}'


class IngredientsShipment(Base):
    __tablename__ = 'ingredient_shipments'
    id = Column(Integer, primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    quantity = Column(Float)
    measure_id = Column(Integer, ForeignKey('measures.id'))
    price = Column(Float)

    def __repr__(self) -> str:
        return f'IngredientsShipment id: {self.id}, ingredient_id: {self.ingredient_id}, quantity: {self.quantity}, ' \
               f'measure_id: {self.measure_id}, price: {self.price}'


class Measure(Base):
    __tablename__ = 'measures'
    id = Column(Integer, primary_key=True)
    title = Column(String)

    def __repr__(self) -> str:
        return f'Measure id: {self.id}, title: {self.title}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
