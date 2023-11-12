from flask import render_template, redirect, url_for, flash, request,current_app

from __init__ import db, app, photos, login_manager,os
from .models import Brand, Category, Product
from shop.products.forms import Add_Product
from flask_login import login_required, current_user
from shop.admin.models import User
from shop.cart.models import Cart


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route('/add-brand', methods=['GET', 'POST'])
@login_required
def addbrand():
    if current_user.role != 'admin':
        return redirect(url_for('login'))

    if request.method == 'POST':
        get_brand = request.form.get('brand')
        brand = Brand(name=get_brand)
        db.session.add(brand)
        flash(f'{get_brand} added')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('products/add-brand.html')


@app.route('/add-category', methods=['GET', 'POST'])
def add_category():
    categories = Category.query.all()
    if request.method == 'POST':
        get_category = request.form.get('category')
        category = Category(name=get_category)
        db.session.add(category)

        db.session.commit()
        return redirect(url_for('category'))
    return render_template('products/add-category.html')


@app.route('/admin/category/index', methods=['GET', 'POST'])
def category():
    categories = Category.query.all()
    return render_template('admin/category/index.html', categories=categories)


@app.route('/add-product', methods=['POST', 'GET'])
@login_required
def add_product():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Add_Product(request.form)
    if request.method == 'POST':
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        description = form.description.data
        author = form.author.data
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'))
        addpro = Product(name=name, price=price, discount=discount, stock=stock, description=description,
                         category_id=category, image_1=image_1, author=author)
        db.session.add(addpro)
        db.session.commit()
        return redirect(url_for('product_manager'))
    return render_template('products/add-product.html', form=form, categories=categories, brands=brands)


@app.route('/admin/category/delete/<int:id>', methods=['GET', 'POST'])
def delete_category(id):
    delete_category = Category.query.get(id)
    if request.method == 'POST':
        db.session.delete(delete_category)
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('admin/category/delete.html', category=delete_category)


@app.route('/admin/category/edit/<int:id>', methods=['POST', 'GET'])
def edit_category(id):
    edit_category = Category.query.get(id)
    if request.method == 'POST':
        edit_category.name = request.form.get('name')
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('admin/category/edit.html', category=edit_category)


@app.route('/product/index', methods=['POST', 'GET'])
def product_page():
    page= request.args.get('page',1,type=int)
    category = Category.query.all()
    products = Product.query.paginate(page=page,per_page=6)


    return render_template('products/index.html', products=products, categories=category)


@app.route('/product/index/<int:id>')
def product_filter(id):
    products = Product.query.filter_by(category_id=id).all()
    title = Category.query.filter_by(id=id).first()
    categories = Category.query.all()

    return render_template('products/filter-by-category.html', products=products, categories=categories, title=title)


@app.route('/admin/product/manager')
def product_manager():
    products = Product.query.all()

    return render_template('admin/products/index.html', products=products)


@app.route('/admin/product/edit/<int:id>', methods=['POST', 'GET'])
def edit_product(id):
    edit_product = Product.query.get(id)
    categories=Category.query.all()
    if request.method == 'POST':
        edit_product.name = request.form.get('name')
        edit_product.price=request.form.get('price')
        edit_product.category_id=request.form.get('category_id')
        edit_product.description = request.form.get('description')
        edit_product.stock= request.form.get('stock')
        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path,'static/images'+ edit_product.image_1))
                edit_product.image_1 = photos.save(request.files.get('image_1'))
            except:
                edit_product.image_1 = photos.save(request.files.get('image_1'))


        db.session.commit()
        return redirect(url_for('product_page'))
    return render_template('admin/products/edit.html', product=edit_product,categories=categories)


@app.route('/admin/product/delete/<int:id>', methods=['GET', 'POST'])
def delete_product(id):
    delete_product = Product.query.get(id)

    if request.method == 'POST':
        db.session.delete(delete_product)
        db.session.commit()
        return redirect(url_for('product_manager'))
    return render_template('admin/products/delete.html', delete_product=delete_product)


@app.route('/detail/<int:id>', methods=['GET', 'POST'])
def product_detail(id):
    product = Product.query.get(id)

    if request.method == 'POST':
        if current_user.is_authenticated:
            user_cart = Cart.query.filter_by(user_id=current_user.id, product_id=product.id).first()
            cart = Cart(user_id=current_user.id, product_id=product.id)
            if user_cart is None:
                cart = Cart(user_id=current_user.id, product_id=product.id, count=request.form.get('count'))
                db.session.add(cart)
                db.session.commit()
                flash(f'Sản phẩm đã được thêm vào giỏ hàng', 'success')
            else:
                user_cart.count = user_cart.count + 1
                db.session.commit()
                flash(f'Sản phẩm đã được thêm vào giỏ hàng', 'success')
        else:
            flash('Bạn cần đăng nhập để thêm sản phẩm vào giỏ hàng', 'warning')
            return redirect(url_for('login'))

    return render_template('products/details.html', product=product)
