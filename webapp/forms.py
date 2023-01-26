from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, TelField, DateField, TextAreaField, IntegerField, TimeField
from wtforms.validators import DataRequired

class OrderingAddForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()], render_kw={'class': 'form-control'})
    adress = StringField('Адрес', validators=[DataRequired()], render_kw={'class': 'form-control', 'placeholder': 'Улица'})
    entrance = IntegerField('Подъезд', validators=[DataRequired()], render_kw={'class': 'form-control', 'placeholder': 'Номер подъезда'})
    floor = IntegerField('Этаж', validators=[DataRequired()], render_kw={'class': 'form-control', 'placeholder': 'Этаж'})
    apartment = IntegerField('Квартира', validators=[DataRequired()], render_kw={'class': 'form-control', 'placeholder': 'Номер квартиры'})
    phone = TelField('Телефон', validators=[DataRequired()], render_kw={'class': 'form-control'})
    date = DateField('Дата', validators=[DataRequired()], render_kw={'class': 'form-control'})
    time = TimeField('Время', validators=[DataRequired()], render_kw={'class': 'form-control'})
    comment = TextAreaField('Комментарий', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Подтвердить заказ', validators=[DataRequired()], render_kw={'class': 'form-control'})
