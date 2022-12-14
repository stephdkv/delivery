from webapp.models import (db, Address, User, Product, ProductCategory, Category,
                           Basket, BasketProduct, Order, Delivery, PickupPoint, Employer,
                           Position, ProductIngredient, Ingredient, IngredientsShipment, Measure)
from flask import Flask, render_template, request, redirect


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)

    def get_address_fields(inputRequest):
        return {'name': inputRequest.form['name'], 'city': inputRequest.form['city'],
                'street': inputRequest.form['street'], 'house': inputRequest.form['house'],
                'apartment': inputRequest.form['apartment'], 'user_id': inputRequest.form['user_id']}

    @app.route('/admin/address/add', methods=['GET', 'POST'])
    def address_add():
        if request.method == 'GET':
            return render_template('address_add.html')
        address = get_address_fields(request)
        new_address = Address(name=address['name'], city=address['city'], street=address['street'],
                              house=address['house'], apartment=address['apartment'],
                              user_id=address['user_id'])
        try:
            db.session.add(new_address)
            db.session.commit()
            return redirect('/admin/address/add')
        except:
            return "There was a problem adding new stuff."

    @app.route('/admin/address/update/<int:id>', methods=['POST'])
    def address_update():
        address = get_address_fields(request)

        new_address = Address(name=address['name'], city=address['city'], street=address['street'],
                              house=address['house'], apartment=address['apartment'],
                              user_id=address['user_id'])
        try:
            db.session.(new_address)
            db.session.commit()
            return redirect('/admin/address/add')
        except:
            return "There was a problem adding new stuff."

    @app.route('/admin/address/get/<int:id>')
    def address_get(id: int):
        try:
            address = Address.query.get_or_404(id)
            return render_template('index.html', address=address)
        except:
            return "There was a problem deleting data."

    @app.route('/admin/address/delete/<int:id>')
    def address_delete(id: int):
        address = Address.query.get_or_404(id)
        try:
            db.session.delete(address)
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem deleting data."

    return app
