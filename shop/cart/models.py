from __init__ import db


class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    count = db.Column(db.Integer, nullable=False)
    product = db.relationship('Product', backref=db.backref('cart', lazy=True),
                              primaryjoin='Cart.product_id==Product.id')
    user = db.relationship('User', lazy=True)


class OrderHeader(db.Model):
    __tablename__ = 'OrderHeader'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))

    user_cart = db.relationship('Cart', backref=db.backref('order', lazy=True),
                                primaryjoin='OrderHeader.cart_id==Cart.id')
    user = db.relationship('User', lazy=True)
    order_date = db.Column(db.Date, unique=False)
    ship_date = db.Column(db.Date, unique=False)
    order_status = db.Column(db.String(20), unique=False, nullable=False)


class OrderDetail(db.Model):
    __tablename__ = 'OrderDetail'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product = db.relationship('Product', backref=db.backref('order', lazy=True),
                              primaryjoin='OrderDetail.product_id==Product.id')
    count = db.Column(db.Integer)
    order_id = db.Column(db.Integer,db.ForeignKey('OrderHeader.id'))
    order = db.relationship('OrderHeader', backref=db.backref('orderdetail',lazy=True),
                            primaryjoin='OrderDetail.order_id==OrderHeader.id')

