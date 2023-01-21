from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired


class DeliveryAddForm(FlaskForm):
    order_id = SelectField(u'Заказ', coerce=int, render_kw={"class": "form-select"})
    done = BooleanField('Отгружен', default=False, render_kw={"class": "form-check-input"})
    address_id = SelectField(u'Адрес', coerce=int, render_kw={"class": "form-select"})
    pickup_point_id = SelectField(u'Точка выдачи', coerce=int, render_kw={"class": "form-select"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})


class DeliveryUpdateForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()], render_kw={"class": "form-control", 'disabled': 'disabled'})
    order_id = SelectField(u'Заказ', coerce=int, render_kw={"class": "form-select"})
    done = BooleanField('Отгружен', default=False, render_kw={"class": "form-check-input"})
    address_id = SelectField(u'Адрес', coerce=int, render_kw={"class": "form-select"})
    pickup_point_id = SelectField(u'Точка выдачи', coerce=int, render_kw={"class": "form-select"})
    is_active = BooleanField('Активный', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})
