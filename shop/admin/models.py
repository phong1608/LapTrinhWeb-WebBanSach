from flask_login import UserMixin

from __init__ import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    role = db.Column(db.String(20), unique=False, nullable=False)
    address = db.Column(db.String(100), unique=False, nullable=True)
    contact = db.Column(db.String(100), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.name
