from flask import Blueprint, render_template

from webapp import config
from webapp.admin.decorators import admin_required
from webapp.admin.pickup_point.forms import PickupPointForm
from webapp.models import db
from webapp.admin.pickup_point.models import PickupPoint

blueprint = Blueprint('pickup_point', __name__, url_prefix='/admin/pickup_point')


@blueprint.route('/add')
@admin_required
def add():
    title = 'Добавление пункта выдачи'
    form = PickupPointForm()
    return render_template(
        "admin/pickup_point/add.html",
        page_title=title,
        form=form,
        menu=config.ADMIN_NAVBAR,
    )


@blueprint.route('/process-add')
@admin_required
def process_add(data):
    new_pickup_point = PickupPoint(
        title=data['title'],
        city=data['city'],
        street=data['street'],
        house=data['house'],
    )
    db.session.add(new_pickup_point)
    db.session.commit()


@blueprint.route('/process-update')
@admin_required
def proces_update(pickup_point_id: int, data: dict) -> None:
    edited_pickup_point = db.session.query(PickupPoint).filter_by(id=pickup_point_id).first()
    if edited_pickup_point is not None:
        edited_pickup_point.title = data['title'],
        edited_pickup_point.city = data['city'],
        edited_pickup_point.street = data['street'],
        edited_pickup_point.house = data['house'],
        db.session.add(edited_pickup_point)
        db.session.commit()


@blueprint.route('/process-delete')
@admin_required
def proces_delete(pickup_point_id: int) -> None:
    deleted_pickup_point = db.session.query(PickupPoint).filter_by(id=pickup_point_id).first()
    if deleted_pickup_point is not None:
        db.session.delete(deleted_pickup_point)
        db.session.commit()


@blueprint.route('/list')
@admin_required
def show_list():
    title = 'Список пунктов выдачи'
    point_list = PickupPoint.query.order_by(PickupPoint.id.asc()).all()
    return render_template('admin/pickup_point/list.html', page_title=title, point_list=point_list)

# def get(pickup_point_id: int) -> PickupPoint | None:
#     return db.session.query(PickupPoint).filter_by(id=pickup_point_id).first()
