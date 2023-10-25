from __init__ import db


class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    count = db.Column(db.Integer,nullable=False)
    product = db.relationship('Product', backref=db.backref('cart', lazy=True), primaryjoin='Cart.product_id==Product.id')
    user = db.relationship('User',lazy=True)


