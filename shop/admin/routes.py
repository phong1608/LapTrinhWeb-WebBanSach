from flask import render_template, redirect, url_for, flash, request
from __init__ import db, app, photos,login_manager,bcrypt
from shop.forms import RegistrationForm, LoginForm
from shop.admin.models import User

from shop.cart.models import Cart,OrderHeader,OrderDetail
@app.route('/admin/register')
def admin_register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, password=hash_password, email=form.email.data,role='admin')
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('admin/register.html', form=form)

