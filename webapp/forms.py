from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, TelField, DateField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class OrderingAddForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()], render_kw={'class': 'form-control'})
    adress = StringField('Адрес', validators=[DataRequired()], render_kw={'class': 'form-control', 'placeholder': 'Улица'})
    entrance = StringField('Подъезд', validators=[DataRequired()], render_kw={'class': 'form-control', 'placeholder': 'Номер подъезда'})
    floor = StringField('Этаж', validators=[DataRequired()], render_kw={'class': 'form-control', 'placeholder': 'Этаж'})
    apartment = StringField('Квартира', validators=[DataRequired()], render_kw={'class': 'form-control', 'placeholder': 'Номер квартиры'})
    phone = StringField('Телефон', validators=[DataRequired()], render_kw={'class': 'form-control'})
    date = StringField('Дата', validators=[DataRequired()], render_kw={'class': 'form-control'})
    time = StringField('Время', validators=[DataRequired()], render_kw={'class': 'form-control'})
    comment = StringField('Комментарий', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = StringField('Подтвердить заказ', validators=[DataRequired()], render_kw={'class': 'form-control'})
