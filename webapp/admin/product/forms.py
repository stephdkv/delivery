from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class ProductAddForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()], render_kw={"class": "form-control"})
    price = IntegerField('Цена', validators=[DataRequired()], render_kw={"class": "form-control"})
    description = TextAreaField('Описание', validators=[DataRequired()], render_kw={"class": "form-control"})
    calories = IntegerField('Колличество каллорий', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})


class ProductUpdateForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()], render_kw={"class": "form-control", 'disabled': 'disabled'})
    title = StringField('Название', validators=[DataRequired()], render_kw={"class": "form-control"})
    price = IntegerField('Цена', validators=[DataRequired()], render_kw={"class": "form-control"})
    description = TextAreaField('Описание', validators=[DataRequired()], render_kw={"class": "form-control"})
    calories = IntegerField('Колличество каллорий', validators=[DataRequired()], render_kw={"class": "form-control"})
    is_active = BooleanField('Активный', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})