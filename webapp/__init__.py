from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate


from webapp.forms import OrderingAddForm
from webapp.models import OrderingForm
from flask import flash


from webapp.user.models import User
from webapp.models import db
from webapp.user.views import blueprint as user_blueprint
from webapp.admin.address.views import blueprint as address_blueprint
from webapp.admin.delivery.views import blueprint as delivery_b_blueprint
from webapp.admin.pickup_point.views import blueprint as pickup_point_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(user_blueprint)
    app.register_blueprint(pickup_point_blueprint)
    app.register_blueprint(delivery_b_blueprint)
    app.register_blueprint(address_blueprint)

    @app.route('/ordering', methods=['POST', 'GET'])
    def process_ordering():
        form = OrderingAddForm()
        if form.validate_on_submit():
            new_ordering_form = OrderingForm(
                name=form.name.data,
                adress=form.adress.data,
                entrance=form.entrance.data,
                floor=form.floor.data,
                apartment=form.apartment.data,
                phone=form.phone.data,
                date=form.phone.data,
                time=form.time.data,
                comment=form.comment.data
            )
            db.session.add(new_ordering_form)
            db.session.commit()
            flash('Вы успешно сделали заказ!')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash('Ошибка в поле {}: {}'.format(
                        getattr(form, field).label.text,
                        error
                    ))
        return render_template('ordering.html')


    @app.route("/")
    def index():
        pass

    return app
