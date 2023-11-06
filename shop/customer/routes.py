from flask import render_template, redirect, url_for, flash, request
from __init__ import db, app, photos
from flask_login import login_required,current_user,logout_user,login_user




@app.route('/profile',methods=['POST','GET'])
@login_required
def profile():
    if request.method=='POST':
        current_user.name=request.form.get('name')
        current_user.email=request.form.get('email')
        current_user.contact=request.form.get('contact')
        current_user.address=request.form.get('address')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('/customer/profile.html')