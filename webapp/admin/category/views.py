from flask import Blueprint, render_template, abort, redirect, url_for

from werkzeug import Response

from webapp import config
from webapp.admin.decorators import admin_required
from webapp.admin.category.forms import CategoryAddForm, CategoryUpdateForm
from webapp.models import db
from webapp.admin.category.models import Category

blueprint = Blueprint('category', __name__, url_prefix='/admin/category')

@blueprint.route('/add')
@admin_required
def add() -> str:
    title = 'Добавление категории'
    form = CategoryAddForm()
    return render_template(
        "admin/category/add.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
    )

@blueprint.route('/process-add', methods=['POST'])
@admin_required
def process_add() -> Response:
    form = CategoryAddForm()
    new_category = Category(
        title=form.title.data,
        is_active=True,
    )
    db.session.add(new_category)
    db.session.commit()
    return redirect(url_for('category.show_list'))

@blueprint.route('/update/<int:category_id>')
@admin_required
def update(category_id: int) -> str:
    title = 'Изменение адреса'
    category = Category.query.filter(Category.id == category_id).first()
    form = CategoryUpdateForm(
        title=category.city,
        is_active=category.is_active,
    )
    if not category:
        abort(404)
    return render_template(
        "admin/pickup_point/update.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
        data=category
    )

@blueprint.route('/process-update')
@admin_required
def process_update(category_id: int) -> Response:
    form = CategoryUpdateForm()
    edited_category = db.session.query(Category).filter_by(id=category_id).first()
    if edited_category is not None:
        edited_category.title = form.title.data,
        edited_category.is_active = form.is_active.data,
        db.session.add(edited_category)
        db.session.commit()
    return redirect(url_for('category.show_list'))


@blueprint.route('/process-delete/<int:category_id>')
@admin_required
def process_delete(category_id: int) -> Response:
    deleted_category = db.session.query(Category).filter_by(id=category_id).first()
    deleted_category.is_active = False
    if deleted_category is not None:
        db.session.add(deleted_category)
        db.session.commit()
    return redirect(url_for('pickup_point.show_list'))


@blueprint.route('/list')
@admin_required
def show_list():
    title = 'Список категорий'
    category_list = Category.query.filter_by(is_active=True).order_by(Category.id.asc()).all()
    return render_template(
        'admin/category/list.html',
        page_title=title,
        category_list=category_list,
        menu=config.ADMIN_NAVBAR,
    )