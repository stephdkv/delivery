from flask import Blueprint, render_template, abort, redirect, url_for
from werkzeug import Response

from webapp import config
from webapp.admin.decorators import admin_required
from webapp.admin.pickup_point.forms import PickupPointAddForm, PickupPointUpdateForm
from webapp.models import db
from webapp.admin.pickup_point.models import PickupPoint

blueprint = Blueprint('pickup_point', __name__, url_prefix='/admin/pickup_point')


@blueprint.route('/add')
@admin_required
def add() -> str:
    title = 'Добавление пункта выдачи'
    form = PickupPointAddForm()
    return render_template(
        "admin/pickup_point/add.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
    )


@blueprint.route('/process-add', methods=['POST'])
@admin_required
def process_add() -> Response:
    form = PickupPointAddForm()
    new_pickup_point = PickupPoint(
        title=form.title.data,
        city=form.city.data,
        street=form.street.data,
        house=form.house.data,
        is_active=True,
    )
    db.session.add(new_pickup_point)
    db.session.commit()
    return redirect(url_for('pickup_point.show_list'))


@blueprint.route('/update/<int:pickup_point_id>')
@admin_required
def update(pickup_point_id: int) -> str:
    title = 'Изменение пункта выдачи'
    pickup_point = PickupPoint.query.filter(PickupPoint.id == pickup_point_id).first()
    form = PickupPointUpdateForm(
        id=pickup_point.id,
        title=pickup_point.title,
        city=pickup_point.city,
        street=pickup_point.street,
        house=pickup_point.house,
        is_active=pickup_point.is_active,
    )
    if not pickup_point:
        abort(404)
    return render_template(
        "admin/pickup_point/update.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
        data=pickup_point
    )


@blueprint.route('/process-update')
@admin_required
def process_update(pickup_point_id: int) -> Response:
    form = PickupPointUpdateForm()
    edited_pickup_point = db.session.query(PickupPoint).filter_by(id=pickup_point_id).first()
    if edited_pickup_point is not None:
        edited_pickup_point.title = form.title.data,
        edited_pickup_point.city = form.city.data,
        edited_pickup_point.street = form.street.data,
        edited_pickup_point.house = form.house.data,
        edited_pickup_point.is_active = form.is_active.data,
        db.session.add(edited_pickup_point)
        db.session.commit()
    return redirect(url_for('pickup_point.show_list'))


@blueprint.route('/process-delete/<int:pickup_point_id>')
@admin_required
def process_delete(pickup_point_id: int) -> Response:
    deleted_pickup_point = db.session.query(PickupPoint).filter_by(id=pickup_point_id).first()
    deleted_pickup_point.is_active = False
    if deleted_pickup_point is not None:
        db.session.add(deleted_pickup_point)
        db.session.commit()
    return redirect(url_for('pickup_point.show_list'))


@blueprint.route('/list')
@admin_required
def show_list():
    title = 'Список пунктов выдачи'
    point_list = PickupPoint.query.filter_by(is_active=True).order_by(PickupPoint.id.asc()).all()
    return render_template(
        'admin/pickup_point/list.html',
        page_title=title,
        point_list=point_list,
        menu=config.ADMIN_NAVBAR,
    )
