from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product    # Імпортуємо базу даних і модель Product

bp = Blueprint('routes', __name__)   # Створюємо Blueprint з назвою 'routes'    # __name__ потрібен Flask для коректного визначення шляху

@bp.route('/')   # Маршрут для головної сторінки
def index():
    return render_template('index.html')   # Повертаємо HTML-шаблон index.html

@bp.route('/products')    # Маршрут для сторінки зі списком продуктів
def products():
    products = Product.query.all()   # Отримуємо всі записи з таблиці Product
    return render_template('product_list.html', products=products)   # Передаємо список продуктів у шаблон product_list.html

@bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        product = Product(name=name, price=float(price))
        db.session.add(product)
        db.session.commit()
        flash('Product added!')
        return redirect(url_for('routes.products'))
    return render_template('product_form.html', action='Add', product=None)


@bp.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted!')
    return redirect(url_for('routes.products'))


@bp.route('/update/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        product.name = request.form['name']
        product.price = float(request.form['price'])
        product.description = request.form['description']
        product.stock = int(request.form['stock'])
        product.is_active = bool(request.form.get('is_active'))
        product.category = request.form['category']
        product.rating = float(request.form['rating'])
        product.sale = float(request.form['sale'])

        print(f'''name={product.name}, price={product.price}, 
description={product.description}, stock={product.stock}, 
is_active={product.is_active}, category={product.category}, 
rating={product.rating}, sale={product.sale}''')

        db.session.commit()
        flash('Product updated!')
        return redirect(url_for('routes.product'))

    return render_template('product_form.html', action='Update', product=product)
