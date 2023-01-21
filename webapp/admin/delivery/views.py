from flask import Blueprint, render_template, abort, redirect, url_for

from werkzeug import Response

from webapp import config
from webapp.admin.decorators import admin_required
from webapp.admin.delivery.forms import DeliveryAddForm, DeliveryUpdateForm
from webapp.admin.pickup_point.models import PickupPoint
from webapp.models import db
from webapp.admin.delivery.models import Delivery

blueprint = Blueprint('delivery', __name__, url_prefix='/admin/delivery')


@blueprint.route('/add')
@admin_required
def add() -> str:
    title = 'Добавление доставки'
    form = DeliveryAddForm()
    form.order_id.choices = [(order.id, order.name) for order in Order.query.order_by('id')]
    form.address_id.choices = [(address.id, address.name) for address in Address.query.order_by('id')]
    form.pickup_point_id.choices = [
        (pickup_point.id, pickup_point.name) for pickup_point in PickupPoint.query.order_by('id')
    ]
    return render_template(
        "admin/delivery/add.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
    )


@blueprint.route('/process-add', methods=['POST'])
@admin_required
def process_add() -> Response:
    form = DeliveryAddForm()
    new_delivery = Delivery(
        order_id=form.order_id.data,
        done=form.done.data,
        address_id=form.address_id.data,
        pickup_point_id=form.pickup_point_id.data,
        is_active=True,
    )
    db.session.add(new_delivery)
    db.session.commit()
    return redirect(url_for('delivery.show_list'))


@blueprint.route('/update/<int:delivery_id>')
@admin_required
def update(delivery_id: int) -> str:
    title = 'Изменение доставки'
    delivery = Delivery.query.filter(Delivery.id == delivery_id).first()
    form = DeliveryUpdateForm(
        order_id=delivery.order_id,
        done=delivery.done,
        address_id=delivery.address_id,
        pickup_point_id=delivery.pickup_point_id,
        is_active=delivery.is_active,
    )
    form.order_id.choices = [(order.id, order.name) for order in Order.query.order_by('id')]
    form.address_id.choices = [(address.id, address.name) for address in Address.query.order_by('id')]
    form.pickup_point_id.choices = [
        (pickup_point.id, pickup_point.name) for pickup_point in PickupPoint.query.order_by('id')
    ]
    if not delivery:
        abort(404)
    return render_template(
        "admin/delivery/update.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
        data=delivery
    )


@blueprint.route('/process-update')
@admin_required
def proces_update(delivery_id: int) -> Response:
    form = DeliveryUpdateForm()
    edited_delivery = db.session.query(Delivery).filter_by(id=delivery_id).first()
    if edited_delivery is not None:
        edited_delivery.order_id = form.order_id.data,
        edited_delivery.done = form.done.data,
        edited_delivery.address_id = form.address_id.data,
        edited_delivery.pickup_point_id = form.pickup_point_id.data,
        edited_delivery.is_active = form.is_active.data,
        db.session.add(edited_delivery)
        db.session.commit()
    return redirect(url_for('delivery.show_list'))


@blueprint.route('/process-delete/<int:delivery_id>')
@admin_required
def process_delete(delivery_id: int) -> Response:
    deleted_delivery = db.session.query(Delivery).filter_by(id=delivery_id).first()
    deleted_delivery.is_active = False
    if deleted_delivery is not None:
        db.session.add(deleted_delivery)
        db.session.commit()
    return redirect(url_for('delivery.show_list'))


@blueprint.route('/list')
@admin_required
def show_list():
    title = 'Список доставок'
    point_list = Delivery.query.filter_by(is_active=True).order_by(Delivery.id.asc()).all()
    return render_template(
        'admin/delivery/list.html',
        page_title=title,
        point_list=point_list,
        menu=config.ADMIN_NAVBAR,
    )
