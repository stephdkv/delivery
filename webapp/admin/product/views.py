from flask import Blueprint, render_template, abort, redirect, url_for, request, json

from werkzeug import Response

from webapp import config, Category
from webapp.admin.decorators import admin_required
from webapp.admin.order.models import Basket, BasketProduct
from webapp.admin.product.forms import ProductAddForm, ProductUpdateForm
from webapp.models import db
from webapp.admin.product.models import Product

blueprint = Blueprint('product', __name__, url_prefix='/admin/product')


@blueprint.route('/add')
@admin_required
def add() -> str:
    title = 'Добавление товаров'
    form = ProductAddForm()
    form.categories.choices = [(categories.id, categories.title) for categories in
                               Category.query.filter_by(is_active=True).all()]
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
    deleted_product = Product.query.filter_by(id=product_id).first()
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


@blueprint.route('/process-add-from-main', methods=['POST'])
def process_add_from_main():
    print(request.data)
    post = request.json
    basket = Basket.query.filter(
        post['user_id'] == Basket.user_id,
        Basket.is_ordered == False,
    ).first()
    product = Product.query.filter_by(id=post['product_id']).first()
    if basket is not None:
        basket_products = BasketProduct.query.filter_by(basket_id=basket.id).all()
        is_product_row_set = False
        for basket_product in basket_products:
            if basket_product.product_id == product.id:
                basket_product.quantity += 1
                db.session.add(basket_product)
                is_product_row_set = True

        if not is_product_row_set:
            new_basket_product = BasketProduct(
                basket_id=basket.id,
                product_id=product.id,
                quantity=1,
                base_price=product.price,
                final_price=product.price,
                is_active=True,
            )
            db.session.add(new_basket_product)
        db.session.commit()
        total = sum([basket_product.final_price * basket_product.quantity for basket_product in basket_products])
        count_products_types = len(basket_products)
        basket.total = total
        db.session.add(basket)
        db.session.commit()
    else:
        new_basket = Basket(
            user_id=post['user_id'],
            is_ordered=False,
            total=product.price,
            is_active=True,
        )
        db.session.add(new_basket)
        db.session.commit()
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
        count_products_types = 1
    return json.dumps({'count_products_types': count_products_types})
