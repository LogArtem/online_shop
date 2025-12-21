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