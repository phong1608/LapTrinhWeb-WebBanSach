from flask import Flask, flash
from flask import render_template, session, request, redirect, url_for
from __init__ import db, bcrypt, app
import routes
from shop.customer import routes
from shop.cart import routes
from shop.order import routes
from shop.forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from shop.admin.models import User
from shop.customer.models import Register
from shop.products import routes
from shop.Review import routes
from __init__ import login_manager
from shop.customer.forms import Registration
from flask_login import login_user, logout_user, current_user


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/admin/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, password=hash_password, email=form.email.data, role='admin')

        db.session.add(user)
        db.session.commit()
        flash(f'Thanks for registering', 'success')
        return redirect(url_for('index'))
    return render_template('admin/login/register.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def customer_register():
    form = Registration(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, password=hash_password, email=form.email.data, role='customer',contact=form.contact.data,address=form.address.data)

        db.session.add(user)
        db.session.commit()
        flash(f'Thanks for registering', 'success')
        return redirect(url_for('index'))
    return render_template('customer/register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():

        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash(f'Welcome {form.email.data}', 'success')
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Wrong password or email', 'danger')
    return render_template('login.html', form=form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
