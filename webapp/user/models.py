from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.models import db


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birthday = db.Column(db.Date)
    username = db.Column(db.String)
    phone = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True)
    register_day = db.Column(db.Date)
    password = db.Column(db.String(128))
    role = db.Column(db.String(255))
    # addresses = relationship("Address")
    # orders = relationship("Order")
    # baskets = relationship("Basket")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User {}>'.format(self.username)
