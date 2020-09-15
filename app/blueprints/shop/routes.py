from .import bp as shop
from flask import flash, request, render_template, redirect, url_for, session, jsonify
from app.blueprints.shop.models import Product
import stripe

@shop.route('/')
def get_products():
    context = {
        'products': Product.query.all(),
    }
    return render_template('marketplace.html', **context)

@shop.route('/add')
def add_to_cart():
    _id = int(request.args.get('id'))
    p = Product.query.get(_id)
    item = {
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'image': p.image,
        'in_stock': p.in_stock,
        'description': p.description
    }
    session['cart']['items'].append(item)
    session['cart']['cart_total'] = 0
    for i in session['cart']['items']:
        session['cart']['cart_total'] += i['price']
    flash(f'{p.name} has been added to your cart', 'success')
    return redirect(url_for('shop.get_products'))

@shop.route('/cart')
def cart():
    display_cart = []
    session['cart']['cart_total'] = 0
    for i in session['cart']['items']:
        if i not in display_cart:
            display_cart.append(i)
        session['cart']['cart_total'] += i['price']
    context = {
        'items': display_cart,
        'cart_total': session['cart']['cart_total']
    }
    return render_template('cart.html', **context)

@shop.route('/remove')
def remove_from_cart():
    _id = int(request.args.get('id'))
    for item in session['cart']['items']:
        if _id == item['id']:
            session['cart']['items'].remove(item)
            # session['cart']['cart_total'] -= item['price']
            flash(f"Item has been removed", 'info')
            break
    return redirect(url_for('shop.cart'))

@shop.route('/clear')
def clear_cart():
    session['cart']['items'].clear()
    session['cart']['cart_total'] = 0
    flash('All items have been removed from cart', 'success')
    return redirect(url_for('shop.cart'))

@shop.route('/checkout')
def checkout():
    print("It Works")
    context = {}
    return render_template('checkout.html', **context)

@shop.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    stripe_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data':
            }
        }