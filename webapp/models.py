from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    name = db.Column(db.String)
    is_active = db.Column(db.Boolean)

    def __repr__(self) -> str:
        return f"Review id: {self.id}, text: {self.text}, name: {self.name}"


class MainSliderAction(db.Model):
    __tablename__ = "main_slider_actions"
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer, unique=True)
    heading = db.Column(db.String)
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean)

    def __repr__(self) -> str:
        return f"Review id: {self.id}, position: {self.position}, " \
               f"heading: {self.heading}, description: {self.description}"
