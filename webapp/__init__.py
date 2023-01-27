from flask import Flask, render_template, url_for, request
from flask_login import LoginManager, current_user
from flask_migrate import Migrate

from webapp.forms import OrderingAddForm
from webapp.models import OrderingForm
from flask import flash

from webapp.admin.category.models import Category
from webapp.admin.product.models import Product, ProductCategory
from webapp.admin.order.models import Basket, BasketProduct
from webapp.user.models import User
from webapp.models import db, MainSliderAction, Review
from webapp.user.views import blueprint as user_blueprint
from webapp.admin.address.views import blueprint as address_blueprint
from webapp.admin.category.views import blueprint as category_blueprint
from webapp.admin.delivery.views import blueprint as delivery_b_blueprint
from webapp.admin.order.views import blueprint as order_blueprint
from webapp.admin.pickup_point.views import blueprint as pickup_point_blueprint
from webapp.admin.product.views import blueprint as product_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(user_blueprint)
    app.register_blueprint(address_blueprint)
    app.register_blueprint(category_blueprint)
    app.register_blueprint(delivery_b_blueprint)
    app.register_blueprint(order_blueprint)
    app.register_blueprint(pickup_point_blueprint)
    app.register_blueprint(product_blueprint)

    @app.route('/ordering', methods=['POST', 'GET'])
    def process_ordering():
        form = OrderingAddForm()
        if current_user.is_authenticated:
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
        else:
            pass

        return render_template('ordering.html', form=form)

    @app.route("/")
    def index():
        title = 'Главная'
        carousel_items = MainSliderAction.query.filter_by(is_active=True).order_by(
            MainSliderAction.position.asc()).all()
        reviews = Review.query.filter_by(is_active=True).order_by(Review.id.asc()).all()
        categories = Category.query.filter_by(is_active=True).order_by(Category.id.asc()).all()
        products = Product.query.filter_by(is_active=True).order_by(Product.id.asc()).all()
        product_list = get_product_list_with_category(products, categories)
        return render_template(
            'index.html',
            title=title,
            carousel_items=carousel_items,
            reviews=reviews,
            categories=categories,
            product_list=product_list,
        )

        # @app.route("/basket")
        # def your_basket():
        title = 'Ваша корзина'
        basket_products = get_basket_list_with_product()
        product_ids = [x.product_id for x in basket_products]
        products = Product.query.filter(Product.id.in_(product_ids)).all()
        print(products)
        return render_template(
            'basket.html',
            basket_products=basket_products
        )

    @app.route("/basket")
    def your_basket():
        title = 'Ваша корзина'
        basket_products = get_basket_list_with_product()
        product_ids = [x.product_id for x in basket_products]
        products = Product.query.filter(Product.id.in_(product_ids)).all()
        basket_products_list = []
        for basket_product in basket_products:
            needle_product = None
            for product in products:
                if product.id == basket_product.product_id:
                    needle_product = product
                    # print(needle_product)
            if needle_product is None:
                product_name = 'Не найден'
            else:
                product_name = needle_product.title
                print(product_name)
            basket_product_dict = {
                'id': basket_product.id,
                'basket_id': basket_product.basket_id,
                'product_id': basket_product.product_id,
                'quantity': basket_product.quantity,
                'base_price': basket_product.base_price,
                'final_price': basket_product.final_price,
                'is_active': basket_product.is_active,
                'product_name': product_name
            }
            basket_products_list.append(basket_product_dict)
            print(basket_products_list)

        return render_template(
            'basket.html',
            basket_products_list=basket_products_list,

        )

    @app.route("/menu")
    def title_menu():
        title = 'Меню'
        carousel_items = MainSliderAction.query.filter_by(is_active=True).order_by(
            MainSliderAction.position.asc()).all()
        reviews = Review.query.filter_by(is_active=True).order_by(Review.id.asc()).all()
        categories = Category.query.filter_by(is_active=True).order_by(Category.id.asc()).all()
        products = Product.query.filter_by(is_active=True).order_by(Product.id.asc()).all()
        product_list = get_product_list_with_category(products, categories)
        return render_template(
            'menu.html',
            title=title,
            carousel_items=carousel_items,
            reviews=reviews,
            categories=categories,
            product_list=product_list,
        )

    @app.route('/product_add')
    def product_add():
        return render_template(
            'basket.html'
        )

    def get_category_dict_by_id(category_id: int, categories: list) -> dict | None:
        for category in categories:
            if category.id == category_id:
                return {
                    'id': category.id,
                    'title': category.title,
                    'is_active': category.is_active,
                    'translit': category.translit,
                }
        return None

    def get_product_list_with_category(products: list, categories: list) -> list:
        product_ids = [x.id for x in products]
        product_categories = ProductCategory.query.filter(
            ProductCategory.product_id.in_(product_ids)
        )
        product_list = []
        for product in products:
            product_dict = {
                'id': product.id,
                'title': product.title,
                'price': product.price,
                'description': product.description,
                'calories': product.calories,
                'is_active': product.is_active,
                'categories': []
            }
            for product_category in product_categories:
                if product_category.product_id == product.id:
                    category = get_category_dict_by_id(product_category.category_id, categories)
                    product_dict['categories'].append(category)
            product_list.append(product_dict)
        return product_list

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    def get_basket_list_with_product():
        basket = Basket.query.filter(
            current_user.id == Basket.user_id,
            Basket.is_ordered == False,
        ).first()
        if basket is not None:
            basket_products = BasketProduct.query.filter_by(basket_id=basket.id).all()
            return basket_products
        return []

    return app

