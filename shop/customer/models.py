from __init__ import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from wtforms import Form, BooleanField, StringField, PasswordField, validators


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), unique=False)
    contact = db.Column(db.String(20), unique=False)
    address = db.Column(db.String(30), unique=False)


