from sqlalchemy.orm import relationship

from webapp.models import db


class Delivery(db.Model):
    __tablename__ = "deliveries"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    done = db.Column(db.Boolean)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.id"))
    pickup_point_id = db.Column(db.Integer, db.ForeignKey("pickup_points.id"))
    is_active = db.Column(db.Boolean)
    orders = relationship("Order", lazy="joined")
    pickup_point = relationship("PickupPoint", lazy="joined", primaryjoin="PickupPoint.id == Delivery.pickup_point_id")
    addresses = relationship("Address", lazy="joined")

    def __repr__(self) -> str:
        return (
            f"Delivery id: {self.id}, order_id: {self.order_id}, done: {self.done}, "
            f"address_id: {self.address_id}, pickup_point_id: {self.pickup_point_id}"
        )
