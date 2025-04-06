import uuid
from flask import Blueprint, request, jsonify
from backend.models import Cart, CartItem, Product
from backend.views.auth import token_required
from backend import db

main = Blueprint('buyer_cart', __name__)


# 买家添加商品到购物车API[PUT]  /api/cart/add_product
@main.route('/add_product', methods=['PUT'])
@token_required
def add_product_to_cart(current_user):
    try:
        # Ensure the user is a buyer
        if current_user.role != 'buyer':
            return jsonify({
                "code": 403,
                "message": "Access denied: Only buyers can add products to cart"
            }), 403

        # Get the product ID and quantity from the request
        data = request.get_json()
        if not data or 'proid' not in data or 'quantity' not in data:
            return jsonify({
                "code": 400,
                "message": "Invalid input: Missing required fields 'proid' and 'quantity'"
            }), 400

        # Check if the product exists
        product = Product.query.filter_by(proid=data['proid']).first()
        if not product:
            return jsonify({
                "code": 404,
                "message": f"Product not found with proid: {data['proid']}"
            }), 404

        # Get the cart for the user (if it doesn't exist, create one)
        cart = Cart.query.filter_by(userid=current_user.userid).first()
        if not cart:
            cart = Cart(
                carid=str(uuid.uuid4()),
                userid=current_user.userid
            )
            db.session.add(cart)
            db.session.commit()

        # Check if the user already has the product in their cart
        cart_item = CartItem.query.filter_by(carid=cart.carid, proid=data['proid']).first()
        if cart_item:
            # Update the quantity if the product is already in the cart
            cart_item.quantity += data['quantity']
            db.session.commit()
        else:
            # Add the product to the cart if it's not already there
            cart_item = CartItem(
                carid=cart.carid,
                proid=data['proid'],
                quantity=data['quantity']
            )
            db.session.add(cart_item)
            db.session.commit()

        return jsonify({
            "code": 200,
            "message": "Product added to cart successfully",
            "data": {
                "proid": data['proid'],
                "quantity": data['quantity']
            }
        }), 200  # OK

    except Exception as e:
        print(f"Error: {str(e)}")
        db.session.rollback()
        return jsonify({
            "code": 500,
            "message": f"Error: {str(e)}"
        }), 500  # Internal Server Error


# 买家获取购物车列表API[GET]   /api/cart/list
@main.route('/list', methods=['GET'])
@token_required
def get_cart_list(current_user):
    try:
        # Ensure the user is a buyer
        if current_user.role != 'buyer':
            return jsonify({
                "code": 0,
                "message": "Access denied: Only buyers can view their cart"
            }), 403

        # Get the user's cart
        cart = Cart.query.filter_by(userid=current_user.userid).first()
        if not cart:
            return jsonify({
                "code": 0,
                "message": "Cart is empty"
            }), 400

        # Get the cart items
        cart_items = CartItem.query.filter_by(carid=cart.carid).all()
        if not cart_items:
            return jsonify({
                "code": 0,
                "message": "Cart is empty"
            }), 400

        # Get the product details for each item
        products = []
        for item in cart_items:
            product = Product.query.filter_by(proid=item.proid).first()
            if not product:
                return jsonify({
                    "code": 0,
                    "message": f"Product not found: {item.proid}"
                }), 404

            products.append({
                "proid": product.proid,
                "name": product.name,
                "price": str(product.price),
                "quantity": item.quantity,
                "image": product.image
            })

        # Return the cart list
        return jsonify({
            "code": 200,
            "message": "Cart list retrieved successfully",
            "data": {
                "products": products
            }
        }), 200  # OK

    except Exception as e:
        return jsonify({
            "code": 0,
            "message": f"Error: {str(e)}"
        }), 500  # Internal Server Error
