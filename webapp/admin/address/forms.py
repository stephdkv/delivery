from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, BooleanField, SelectField, StringField
from wtforms.validators import DataRequired


class AddressAddForm(FlaskForm):
    city = StringField('Город', validators=[DataRequired()], render_kw={"class": "form-control"})
    street = StringField('Улица', validators=[DataRequired()], render_kw={"class": "form-control"})
    house = StringField('Дом', validators=[DataRequired()], render_kw={"class": "form-control"})
    apartment = StringField('Квартира', render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})


class AddressUpdateForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()], render_kw={"class": "form-control", 'disabled': 'disabled'})
    city = StringField('Город', validators=[DataRequired()], render_kw={"class": "form-control"})
    street = StringField('Улица', validators=[DataRequired()], render_kw={"class": "form-control"})
    house = StringField('Дом', validators=[DataRequired()], render_kw={"class": "form-control"})
    apartment = StringField('Квартира', render_kw={"class": "form-control"})
    user_id = SelectField(u'Пользователь', coerce=int, render_kw={"class": "form-select"})
    is_active = BooleanField('Активный', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})
