from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired

from webapp.admin.pickup_point.models import PickupPoint


class PickupPointAddForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()], render_kw={"class": "form-control"})
    city = StringField('Город', validators=[DataRequired()], render_kw={"class": "form-control"})
    street = StringField('Улица', validators=[DataRequired()], render_kw={"class": "form-control"})
    house = StringField('Дом', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})


class PickupPointUpdateForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()], render_kw={"class": "form-control", 'disabled': 'disabled'})
    title = StringField('Название', validators=[DataRequired()], render_kw={"class": "form-control"})
    city = StringField('Город', validators=[DataRequired()], render_kw={"class": "form-control"})
    street = StringField('Улица', validators=[DataRequired()], render_kw={"class": "form-control"})
    house = StringField('Дом', validators=[DataRequired()], render_kw={"class": "form-control"})
    is_active = BooleanField('Запомнить меня', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})
