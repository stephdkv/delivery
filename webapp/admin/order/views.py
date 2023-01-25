from datetime import datetime

from flask import Blueprint, render_template, abort, redirect, url_for
from flask_login import current_user

from werkzeug import Response

from webapp import config, User, Product
from webapp.admin.decorators import admin_required
from webapp.admin.order.forms import OrderAddForm, OrderUpdateForm
from webapp.models import db
from webapp.admin.order.models import Order, Basket, BasketProduct

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
    new_basket = Basket(
        user_id=form.user_id.data,
        is_ordered=True,
        total=total,
        is_active=True,
    )
    db.session.add(new_basket)
    db.session.commit()
    new_order = Order(
        basket_id=new_basket.id,
        user_id=form.user_id.data,
        date_time=datetime.now(),
        comment=form.comment.data,
        is_active=True,
    )
    db.session.add(new_order)
    for product in products:
        new_basket_product = BasketProduct(
            basket_id=new_basket.id,
            product_id=product.id,
            quantity=1,
            base_price=product.price,
            final_price=product.price,
            is_active=True,
        )
        db.session.add(new_basket_product)
    db.session.commit()
    return redirect(url_for('order.show_list'))


@blueprint.route('/update/<int:order_id>')
@admin_required
def update(order_id: int) -> str:
    title = 'Изменение заказа'
    order = Order.query.filter(Order.id == order_id).first()
    basket_products = BasketProduct.query.filter_by(basket_id=order.basket_id).all()
    form = OrderUpdateForm(
        id=order.id,
        basket_id=order.basket_id,
        user_id=order.user_id,
        is_active=order.is_active,
        date_time=order.date_time,
        comment=order.comment,
        products=[basket_product.product_id for basket_product in basket_products]
    )
    form.user_id.choices = [(user.id, user.username) for user in User.query.order_by('id')]
    form.products.choices = [(product.id, product.title) for product in Product.query.filter_by(is_active=True).all()]
    if not order:
        abort(404)
    return render_template(
        "admin/order/update.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
        data=order
    )


# todo Незаконченный вариант
@blueprint.route('/process-update', methods=['POST'])
@admin_required
def process_update() -> Response:
    form = OrderUpdateForm()
    edited_order = db.session.query(Order).filter_by(id=form.id.data).first()
    if edited_order is not None:
        edited_order.basket_id = edited_order.basket_id,
        edited_order.user_id = form.user_id.data,
        edited_order.is_active = edited_order.is_active,
        edited_order.comment = form.comment.data,
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
    order_list = Order.query.filter_by(is_active=True).order_by(Order.id.asc()).all()
    return render_template(
        'admin/order/list.html',
        page_title=title,
        order_list=order_list,
        menu=config.ADMIN_NAVBAR,
    )
