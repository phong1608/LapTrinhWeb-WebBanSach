from flask import render_template, redirect, url_for, flash, request
from __init__ import db, app, photos, login_manager
from .models import Cart, OrderHeader, OrderDetail
from shop.products.models import Product
from shop.products.forms import Add_Product
from flask_login import login_required, current_user
from shop.admin.models import User
import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route('/cart')
@login_required
def cart():
    carts = Cart.query.filter_by(user_id=current_user.id)
    total = 0
    for cart in carts:
        total = total + (cart.product.price * cart.count)
    return render_template('customer/cart/index.html', carts=carts, total=total)


@app.route('/emptycart')
def empty_cart():
    flash('Giỏ hàng trống, hãy thêm sản phẩm', 'danger')
    return redirect(url_for('index'))


@app.route('/cart/plus/<int:id>')
def plus(id):
    user_cart = Cart.query.filter_by(id=id).first()
    user_cart.count = user_cart.count + 1
    db.session.commit()
    return redirect(url_for('cart'))


@app.route('/cart/minus/<int:id>')
def minus(id):
    user_cart = Cart.query.filter_by(id=id).first()
    if user_cart.count == 1:
        db.session.delete(user_cart)
        db.session.commit()
    if user_cart.count > 1:
        user_cart.count = user_cart.count - 1
        db.session.commit()
    return redirect(url_for('cart'))


@app.route('/cart/delete/<int:id>')
def delete_cart_item(id):
    user_cart = Cart.query.filter_by(id=id).first()
    db.session.delete(user_cart)
    db.session.commit()
    return redirect(url_for('cart'))


@app.route('/cart/summary', methods=['POST', 'GET'])
def summary():
    carts = Cart.query.filter_by(user_id=current_user.id)
    user = current_user
    total_price = 0
    for cart in carts:
        total_price = total_price + (cart.product.price * cart.count)
    if request.method == 'POST':

        user.email = request.form.get('email')
        user.address = request.form.get('address')
        user.contact = request.form.get('contact')
        
        date = datetime.date.today()
        order_header = OrderHeader(user_id=current_user.id, order_date=date, order_status='Đang xử lý')
        db.session.add(order_header)

        db.session.commit()
        for cart in carts:
            order_detail = OrderDetail(product_id=cart.product_id, order_id=order_header.id, count=cart.count)
            product = Product.query.filter_by(id=order_detail.product_id).first()
            product.stock = product.stock-order_detail.count
            db.session.add(order_detail)
            db.session.delete(cart)
            db.session.commit()

        flash('Đặt hàng thành công', 'success')
        return redirect(url_for('index'))
    return render_template('customer/cart/summary.html', user=user, carts=carts, total=total_price)
