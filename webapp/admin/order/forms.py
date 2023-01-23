from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired


class OrderAddForm(FlaskForm):
    user_id = SelectField(u'Пользователь', coerce=int, render_kw={"class": "form-select"})
    products = SelectMultipleField(
        u'Товары',
        coerce=int,
        render_kw={"class": "form-select", "multiple": True}
    )


class OrderUpdateForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()], render_kw={"class": "form-control", 'disabled': 'disabled'})
    user_id = SelectField(u'Пользователь', coerce=int, render_kw={"class": "form-select"})
    products = SelectMultipleField(
        u'Товары',
        coerce=int,
        render_kw={"class": "form-select", "multiple": True}
    )
