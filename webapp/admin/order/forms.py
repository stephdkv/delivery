from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SelectMultipleField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class OrderAddForm(FlaskForm):
    user_id = SelectField(u'Пользователь', coerce=int, render_kw={"class": "form-select"})
    products = SelectMultipleField(
        u'Товары',
        coerce=int,
        render_kw={"class": "form-select", "multiple": True}
    )
    comment = TextAreaField('Комментарий', render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})


class OrderUpdateForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()], render_kw={"class": "form-control", 'disabled': 'disabled'})
    user_id = SelectField(u'Пользователь', coerce=int, render_kw={"class": "form-select"})
    products = SelectMultipleField(
        u'Товары',
        coerce=int,
        render_kw={"class": "form-select", "multiple": True}
    )
    comment = TextAreaField('Комментарий', render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})
