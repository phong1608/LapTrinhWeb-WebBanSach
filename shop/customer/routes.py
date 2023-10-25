from flask import render_template, redirect, url_for, flash, request
from __init__ import db, app, photos
from flask_login import login_required,current_user,logout_user,login_user


@app.route('/cart/<int:customer_id>',methods=['GET','POST'])
@login_required
def cart():

    return render_template('customer/cart.html')