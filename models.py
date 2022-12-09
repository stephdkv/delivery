from sqlalchemy import (Column, Integer, String, DECIMAL,
                         Date, ForeignKey, Boolean, Text)
from sqlalchemy.orm import relationship
from data_base import Base, engine

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    birthday = Column(Date())
    phone = Column(String(11))
    email = Column(String(120), unique = True)
    registred_day = Column(Date())
    addresses = relationship("Address")
    orders = relationship("Order")
    baskets = relationship("Basket")

    def __repr__(self):
        return f"Client {self.id}, {self.full_name}"

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key = True)
    city = Column(String(30))
    street = Column(String())
    house = Column(String())
    apartment = Column(String())
    user_id = Column(Integer, ForeignKey('user.id'))
    deliveries = relationship("Delivery")

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key = True)
    title = Column(String())
    price = Column(Integer())
    description = Column(Text())
    calories = Column(String())
    baskets = relationship("Basket_product", backref = 'product')
    categories = relationship("Category", secondary = "product_category")

class Product_category(Base):
    __tablename__ = 'product_category'
    product_id = Column(ForeignKey('product.id'), primary_key =True)
    category_id = Column(ForeignKey('category.id'), primary_key =True)
    extra_data = Column(String(100))

    category = relationship("Category", backref = 'product_product_category')
    product = relationship("Product", backref = 'category_product_category')


    

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key = True)
    title = Column(String())

class Basket(Base):
    __tablename__ = 'basket'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    is_ordered = Column(Integer())
    total = Column(DECIMAL())
    orders = relationship("Order")
    products = relationship("Basket_product", backref = 'basket')



class Basket_product(Base):
    __tablename__ = 'basket_product'
    id = Column(Integer, primary_key = True)
    basket_id = Column(Integer, ForeignKey('basket.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer())
    base_price = Column(Integer())
    final_price = Column(DECIMAL())
    extra_data = Column(String(100))


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key = True)
    basket_id = Column(Integer, ForeignKey('basket.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    deliveries = relationship("Delivery")

class Delivery(Base):
    __tablename__ = 'delivery'
    id = Column(Integer, primary_key = True)
    order_id = Column(Integer, ForeignKey('order.id'))
    done = Column(Boolean())
    address_id = Column(Integer, ForeignKey('address.id'))
    pickup_point_id = Column(Integer, ForeignKey('pickup_point.id'))

class Pickup_point(Base):
    __tablename__ = 'pickup_point'
    id = Column(Integer, primary_key = True)
    title = Column(String())
    city = Column(String())
    street = Column(String())
    house = Column(String())
    deliveries = relationship("Delivery")

class Employer(Base):
    __tablename__ = 'employer'
    id = Column(Integer, primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    phone = Column(String(11))
    email = Column(String(120), unique = True)
    registred_day = Column(Date())
    position_id = Column(Integer, ForeignKey('position.id'))


class Position(Base):
    __tablename__ = 'position'
    id = Column(Integer, primary_key = True)
    title = Column(String())
    employers = relationship('employer')
    




if __name__ == '__main__':
    Base.metadata.create_all(bind = engine)
    
