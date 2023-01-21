from sqlalchemy.orm import relationship

from webapp.models import db


class Address(db.Model):
    __tablename__ = "addresses"
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(30))
    street = db.Column(db.String)
    house = db.Column(db.String)
    apartment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    is_active = db.Column(db.Boolean)
    deliveries = relationship("Delivery")
    users = relationship("User")

    def __repr__(self) -> str:
        return (
            f"Address id: {self.id}, city: {self.city}, street: {self.street}, "
            f"house: {self.house}, apartment: {self.apartment}, user_id: {self.user_id}"
        )
