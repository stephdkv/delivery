from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate

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

    @app.route("/")
    def index():
        title = 'Главная'
        return render_template('index.html', carousel_items=[
            {
                'position': 0,
                'heading': 'Тест1',
                'description': 'Тест1  text',
            },
            {
                'position': 1,
                'heading': 'Тест2',
                'description': 'Тест2  text',
            },
        ])



    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
