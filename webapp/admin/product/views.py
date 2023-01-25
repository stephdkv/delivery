from flask import Blueprint, render_template, abort, redirect, url_for

from werkzeug import Response

from webapp import config, Category
from webapp.admin.decorators import admin_required
from webapp.admin.product.forms import ProductAddForm, ProductUpdateForm
from webapp.models import db
from webapp.admin.product.models import Product

blueprint = Blueprint('product', __name__, url_prefix='/admin/product')


@blueprint.route('/add')
@admin_required
def add() -> str:
    title = 'Добавление товаров'
    form = ProductAddForm()
    form.categories.choices = [(categories.id, categories.title) for categories in Category.query.filter_by(is_active=True).all()]
    return render_template(
        "admin/product/add.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
    )


@blueprint.route('/process-add', methods=['POST'])
@admin_required
def process_add() -> Response:
    form = ProductAddForm()
    new_product = Product(
        title=form.title.data,
        price=form.price.data,
        description=form.description.data,
        calories=form.calories.data,
        is_active=True,
        categories=form.categories.data,
    )
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('product.show_list'))


@blueprint.route('/update/<int:product_id>')
@admin_required
def update(product_id: int) -> str:
    title = 'Изменение товара'
    product = Product.query.filter(Product.id == product_id).first()
    form = ProductUpdateForm(
        title=product.title,
        price=product.price,
        description=product.description,
        calories=product.calories,
        is_active=product.is_active,
    )
    if not product:
        abort(404)
    return render_template(
        "admin/product/update.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
        data=product
    )


@blueprint.route('/process-update', methods=['POST'])
@admin_required
def process_update(product_id: int) -> Response:
    form = ProductUpdateForm()
    edited_product = db.session.query(Product).filter_by(id=product_id).first()
    if edited_product is not None:
        edited_product.title = form.title.data,
        edited_product.price = form.price.data,
        edited_product.description = form.description.data,
        edited_product.calories = form.calories.data,
        edited_product.is_active = form.is_active.data,
        db.session.add(edited_product)
        db.session.commit()
    return redirect(url_for('product.show_list'))


@blueprint.route('/process-delete/<int:product_id>')
@admin_required
def process_delete(product_id: int) -> Response:
    deleted_product = db.session.query(Product).filter_by(id=product_id).first()
    deleted_product.is_active = False
    if deleted_product is not None:
        db.session.add(deleted_product)
        db.session.commit()
    return redirect(url_for('product.show_list'))


@blueprint.route('/list')
@admin_required
def show_list():
    title = 'Список товаров'
    product_list = Product.query.filter_by(is_active=True).order_by(Product.id.asc()).all()
    return render_template(
        'admin/product/list.html',
        page_title=title,
        product_list=product_list,
        menu=config.ADMIN_NAVBAR,
    )