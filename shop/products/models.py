from __init__ import db
from sqlalchemy.orm import relationship

class Brand(db.Model):
    __tablename__ = 'Brand'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)


class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)


class Product(db.Model):

    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'), nullable=False)
    description=db.Column(db.String(255), nullable=False, unique=True)
    author=db.Column(db.String(255), nullable=False, unique=False)
    image_1=db.Column(db.String(255))
    category = db.relationship("Category", backref=db.backref('category',lazy=True), primaryjoin="Product.category_id == Category.id")


class Rating(db.Model):

    __tablename__='rating'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    user = db.relationship('User', lazy=True)
    product_id=db.Column(db.Integer,db.ForeignKey('products.id'),nullable=False)
    product = db.relationship('Product', backref=db.backref('rating', lazy=True),
                              primaryjoin='Rating.product_id==Product.id')
    is_rated =db.Column(db.Boolean,default=False,nullable=False)
    
