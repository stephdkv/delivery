from sqlalchemy import (Column, Integer, String, DECIMAL,
                        Date, ForeignKey, Boolean, Text)
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


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String())
    price = Column(Integer())
    description = Column(Text())
    calories = Column(String())
    baskets = relationship('BasketProduct', backref='product')
    categories = relationship('Category', secondary='product_category')


class ProductCategory(Base):
    __tablename__ = 'product_categories'
    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    category_id = Column(ForeignKey('categories.id'))
    extra_data = Column(String(100))
    category = relationship('Category', backref='product_product_category')
    product = relationship('Product', backref='category_product_category')


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    title = Column(String())


class Basket(Base):
    __tablename__ = 'baskets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    is_ordered = Column(Integer())
    total = Column(DECIMAL())
    orders = relationship('Order')
    products = relationship('Basket_product', backref='basket')


class BasketProduct(Base):
    __tablename__ = 'basket_products'
    id = Column(Integer, primary_key=True)
    basket_id = Column(Integer, ForeignKey('baskets.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer())
    base_price = Column(Integer())
    final_price = Column(DECIMAL())
    extra_data = Column(String(100))


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    basket_id = Column(Integer, ForeignKey('baskets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    deliveries = relationship('Delivery')


class Delivery(Base):
    __tablename__ = 'deliveries'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    done = Column(Boolean())
    address_id = Column(Integer, ForeignKey('addresses.id'))
    pickup_point_id = Column(Integer, ForeignKey('pickup_points.id'))


class PickupPoint(Base):
    __tablename__ = 'pickup_points'
    id = Column(Integer, primary_key=True)
    title = Column(String())
    city = Column(String())
    street = Column(String())
    house = Column(String())
    deliveries = relationship('Delivery')


class Employer(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    phone = Column(String(11))
    email = Column(String(120), unique=True)
    register_day = Column(Date())
    position_id = Column(Integer, ForeignKey('positions.id'))


class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    title = Column(String())
    employers = relationship('Employer')


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
