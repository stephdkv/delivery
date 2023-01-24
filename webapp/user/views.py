from datetime import datetime

from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from webapp import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User
from webapp.utils import get_redirect_target

blueprint = Blueprint('user', __name__, url_prefix='/user')


# todo get_redirect_target многократный редирект, возможно убрать

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(get_redirect_target())
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(get_redirect_target())
    flash('Неправильное имя пользователя или пароль')

    return redirect(get_redirect_target())


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    title = "Регистрация"
    return render_template(
        'user/registration.html',
        page_title=title,
        form=form
    )


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        news_user = User(
            #first_name=form.first_name.data,
            #last_name=form.last_name.data,
            username=form.username.data,
            #birthday=form.birthday.data,
            phone=form.phone.data,
            email=form.email.data,
            register_day=datetime.now().date(),
        )
        news_user.set_password(form.password.data)
        db.session.add(news_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле {}: {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('user.register'))
