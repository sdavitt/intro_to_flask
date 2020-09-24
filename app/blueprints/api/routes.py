from .import bp as api
from flask import request, url_for, redirect, jsonify
from app.blueprints.blog.models import Post, User
from app.blueprints.shop.models import Product
from app import db
from datetime import datetime

@api.route('/blog', methods=['GET'])
def get_posts():
    """
    [GET] /api/blog
    """
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

@api.route('/blog/<int:id>', methods=['GET'])
def get_post(id):
    """
    [GET] /api/blog/<id>
    """
    post = Post.query.get(id)
    return jsonify(post.to_dict())

@api.route('/blog', methods=['POST'])
def create_post():
    """
    [POST] /api/blog
    """
    response = request.get_json()
    post = Post()
    post.from_dict(response)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201

@api.route('/blog/<int:id>', methods=['PUT'])
def edit_post(id):
    response = request.get_json()
    post = Post.query.get(id)
    post.body = response.get('body')
    post.updated_on = datetime.utcnow()
    db.session.commit()
    return jsonify(post.to_dict())

@api.route('/blog/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return jsonify([post.to_dict() for post in Post.query.all()])

# @api.route('/blog', methods=['POST'])
# def create_post():
#     """
#     [POST] /api/blog
#     """
#     r = request.get_json()
#     body = r.get('body')
#     user_id = User.query.filter_by(email=r.get('user_id').lower()).first().id
#     p = Post(body=body, user_id=user_id)
#     db.session.add(p)
#     db.session.commit()
#     return jsonify(p.to_dict()), 201

@api.route('/shop', methods=['GET'])
def get_products():
    """
    [GET] /api/shop
    """
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@api.route('/shop/<int:id>', methods=['GET'])
def get_product(id):
    """
    [GET] /api/shop/<id>
    """
    product = Product.query.get(id)
    return jsonify(product.to_dict())

@api.route('/shop', methods=['POST'])
def create_product():
    """
    [POST] /api/shop
    """
    response = request.get_json()
    product = Product()
    product.from_dict(response)
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

@api.route('/shop/<int:id>', methods=['PUT'])
def edit_product(id):
    response = request.get_json()
    product = Product.query.get(id)
    db.session.commit()
    return jsonify(product.to_dict())

@api.route('/shop/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify([product.to_dict() for post in Product.query.all()])