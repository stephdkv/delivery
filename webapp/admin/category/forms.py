from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, BooleanField, SelectField, StringField
from wtforms.validators import DataRequired


class CategoryAddForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})


class CategoryUpdateForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()], render_kw={"class": "form-control", 'disabled': 'disabled'})
    title = StringField('Название', validators=[DataRequired()], render_kw={"class": "form-control"})
    is_active = BooleanField('Активный', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})