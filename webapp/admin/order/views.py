from flask import Blueprint, render_template, abort, redirect, url_for
from flask_login import current_user

from werkzeug import Response

from webapp import config, User, Product
from webapp.admin.decorators import admin_required
from webapp.admin.order.forms import OrderAddForm, OrderUpdateForm
from webapp.models import db
from webapp.admin.order.models import Order, Basket

blueprint = Blueprint('order', __name__, url_prefix='/admin/order')


@blueprint.route('/add')
@admin_required
def add() -> str:
    title = 'Добавление заказа'
    form = OrderAddForm()
    form.user_id.choices = [(user.id, user.username) for user in User.query.all()]
    form.products.choices = [(product.id, product.title) for product in Product.query.filter_by(is_active=True).all()]
    return render_template(
        "admin/order/add.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
    )


@blueprint.route('/process-add', methods=['POST'])
@admin_required
def process_add() -> Response:
    form = OrderAddForm()
    products = Product.query.filter(Product.id.in_(form.products.data)).all()
    total = sum([product.price for product in products])
    print(total)
    new_basket = Basket(
        user_id=form.user_id.data,
        is_ordered=True,
        is_active=True,
    )
    #
    # new_order = Order(
    #     city=form.city.data,
    #     street=form.street.data,
    #     house=form.house.data,
    #     apartment=form.apartment.data,
    #     user_id=current_user.id,
    #     is_active=True,
    # )
    # db.session.add(new_order)
    db.session.commit()
    return redirect(url_for('order.show_list'))


@blueprint.route('/update/<int:order_id>')
@admin_required
def update(order_id: int) -> str:
    title = 'Изменение заказа'
    order = Order.query.filter(Order.id == order_id).first()
    form = OrderUpdateForm(
        city=order.city,
        street=order.street,
        house=order.house,
        apartment=order.apartment,
        user_id=order.user_id,
        is_active=order.is_active,
    )
    form.user_id.choices = [(user.id, user.name) for user in User.query.order_by('id')]
    if not order:
        abort(404)
    return render_template(
        "admin/order/update.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
        data=order
    )


@blueprint.route('/process-update')
@admin_required
def proces_update(order_id: int) -> Response:
    form = OrderUpdateForm()
    edited_order = db.session.query(Order).filter_by(id=order_id).first()
    if edited_order is not None:
        edited_order.city = form.city.data,
        edited_order.street = form.street.data,
        edited_order.house = form.house.data,
        edited_order.apartment = form.apartment.data,
        edited_order.user_id = form.user_id.data,
        edited_order.is_active = form.is_active.data,
        db.session.add(edited_order)
        db.session.commit()
    return redirect(url_for('order.show_list'))


@blueprint.route('/process-delete/<int:order_id>')
@admin_required
def process_delete(order_id: int) -> Response:
    deleted_order = db.session.query(Order).filter_by(id=order_id).first()
    deleted_order.is_active = False
    if deleted_order is not None:
        db.session.add(deleted_order)
        db.session.commit()
    return redirect(url_for('order.show_list'))


@blueprint.route('/list')
@admin_required
def show_list():
    title = 'Список заказов'
    point_list = Order.query.filter_by(is_active=True).order_by(Order.id.asc()).all()
    return render_template(
        'admin/order/list.html',
        page_title=title,
        point_list=point_list,
        menu=config.ADMIN_NAVBAR,
    )
