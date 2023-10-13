from flask import Flask, flash
from flask import render_template, session, request, redirect, url_for
from __init__ import db, bcrypt, app
from shop.forms import RegistrationForm
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from shop.admin.models import User


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, password=hash_password, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()
