from flask import render_template, redirect, url_for, flash, request
from __init__ import db, app, photos, login_manager
from .models import Cart
from shop.products.models import Product
from shop.products.forms import Add_Product
from flask_login import login_required, current_user
from shop.admin.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route('/cart')
def cart():
    carts = Cart.query.filter_by(user_id=current_user.id)

    return render_template('customer/cart/index.html', carts=carts)
