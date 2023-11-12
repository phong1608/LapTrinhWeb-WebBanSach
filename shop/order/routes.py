from flask import render_template, redirect, url_for, flash, request
from __init__ import db, app, photos, login_manager
from shop.cart.models import Cart, OrderHeader, OrderDetail

from flask_login import login_required, current_user
from shop.admin.models import User
import datetime


@app.route('/order-manager', methods=['POST', 'GET'])
@login_required
def order_manager():
    if current_user.role=='admin':
     order_header = OrderHeader.query.all()
    else:
       order_header = OrderHeader.query.filter_by(user_id=current_user.id)
    return render_template('order/index.html', order_header=order_header)


@app.route('/order-manager/detail/<int:id>', methods=['GET', 'POST'])
@login_required
def order_detail(id):
    order_header = OrderHeader.query.filter_by(id=id).first()
    order_detail = OrderDetail.query.filter_by(order_id=id)

    return render_template('order/details.html', order_header=order_header, order_detail=order_detail)


@app.route('/order-manager/update-shipped/<int:id>')
def order_status_shipping(id):
    order_header = OrderHeader.query.filter_by(id=id).first()
    order_detail = OrderDetail.query.filter_by(order_id=id)

    order_header.order_status = 'Đang giao hàng'
    db.session.commit()

    return redirect(url_for('order_detail', id=id))


@app.route('/order-manager/update-shipping/<int:id>')
def order_status_shipped(id):
    order_header = OrderHeader.query.filter_by(id=id).first()
    order_detail = OrderDetail.query.filter_by(order_id=id)

    order_header.order_status = 'Đã giao hàng'
    order_header.ship_date=datetime.date.today()
    db.session.commit()

    return redirect(url_for('order_detail', id=id))


