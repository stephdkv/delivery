from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from webapp.admin.pickup_point.models import PickupPoint


class PickupPointForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()], render_kw={"class": "form-control"})
    city = StringField('Город', validators=[DataRequired()], render_kw={"class": "form-control"})
    street = StringField('Улица', validators=[DataRequired()], render_kw={"class": "form-control"})
    house = StringField('Дом', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})
