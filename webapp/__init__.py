from flask import Flask
from webapp.models import db
from flask import render_template


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    @app.route("/")
    def index():
        return render_template(
            "admin/base.html",
            title="Главная",
            menu=app.config.get('ADMIN_NAVBAR')
        )

    return app
