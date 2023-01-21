from flask import Blueprint, render_template, abort, redirect, url_for
from flask_login import current_user

from werkzeug import Response

from webapp import config, User
from webapp.admin.decorators import admin_required
from webapp.admin.address.forms import AddressAddForm, AddressUpdateForm
from webapp.models import db
from webapp.admin.address.models import Address

blueprint = Blueprint('address', __name__, url_prefix='/admin/address')


@blueprint.route('/add')
@admin_required
def add() -> str:
    title = 'Добавление адреса'
    form = AddressAddForm()
    return render_template(
        "admin/address/add.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
    )


@blueprint.route('/process-add', methods=['POST'])
@admin_required
def process_add() -> Response:
    form = AddressAddForm()
    new_address = Address(
        city=form.city.data,
        street=form.street.data,
        house=form.house.data,
        apartment=form.apartment.data,
        user_id=current_user.id,
        is_active=True,
    )
    db.session.add(new_address)
    db.session.commit()
    return redirect(url_for('address.show_list'))


@blueprint.route('/update/<int:address_id>')
@admin_required
def update(address_id: int) -> str:
    title = 'Изменение адреса'
    address = Address.query.filter(Address.id == address_id).first()
    form = AddressUpdateForm(
        city=address.city,
        street=address.street,
        house=address.house,
        apartment=address.apartment,
        user_id=address.user_id,
        is_active=address.is_active,
    )
    form.user_id.choices = [(user.id, user.name) for user in User.query.order_by('id')]
    if not address:
        abort(404)
    return render_template(
        "admin/address/update.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
        data=address
    )


@blueprint.route('/process-update')
@admin_required
def proces_update(address_id: int) -> Response:
    form = AddressUpdateForm()
    edited_address = db.session.query(Address).filter_by(id=address_id).first()
    if edited_address is not None:
        edited_address.city = form.city.data,
        edited_address.street = form.street.data,
        edited_address.house = form.house.data,
        edited_address.apartment = form.apartment.data,
        edited_address.user_id = form.user_id.data,
        edited_address.is_active = form.is_active.data,
        db.session.add(edited_address)
        db.session.commit()
    return redirect(url_for('address.show_list'))


@blueprint.route('/process-delete/<int:address_id>')
@admin_required
def process_delete(address_id: int) -> Response:
    deleted_address = db.session.query(Address).filter_by(id=address_id).first()
    deleted_address.is_active = False
    if deleted_address is not None:
        db.session.add(deleted_address)
        db.session.commit()
    return redirect(url_for('address.show_list'))


@blueprint.route('/list')
@admin_required
def show_list():
    title = 'Список адресов'
    point_list = Address.query.filter_by(is_active=True).order_by(Address.id.asc()).all()
    return render_template(
        'admin/address/list.html',
        page_title=title,
        point_list=point_list,
        menu=config.ADMIN_NAVBAR,
    )
