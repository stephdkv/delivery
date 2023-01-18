from sqlalchemy.orm import relationship

from webapp import db


class PickupPoint(db.Model):
    __tablename__ = "pickup_points"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    city = db.Column(db.String)
    street = db.Column(db.String)
    house = db.Column(db.String)
    # deliveries = relationship("Delivery")

    def __repr__(self) -> str:
        return (
            f"PickupPoint id: {self.id}, title: {self.title}, city: {self.city}, "
            f"street: {self.street}, house: {self.house}"
        )
