from sqlalchemy.orm import relationship

from webapp.models import db


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    product_categories = relationship("ProductCategory", lazy="joined")

    def __repr__(self) -> str:
        return f"Category id: {self.id}, title: {self.title}"
