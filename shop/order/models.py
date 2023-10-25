from __init__ import db, login_manager


class Order(db.Model):
    id = db.Column(db.Integer(10), nullable=False, unique=True)
    product_id = db.Column(db.Integer(10))
    count = db.Column(db.Interger(10))
    price = db.Column(db.Interger(10))
    product = db.relationship("products", backref=db.backref('product', lazy=True),
                              primaryjoin="Order.product_id == products.id")
    total = db.Column(db.Integer(10))
    description = db.Column(db.String(250))
