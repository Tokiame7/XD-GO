from flask import Blueprint, request, jsonify
from backend.models import Product, Category, User, db
from backend.views.auth import token_required

main = Blueprint('buyer_product', __name__)


# 买家首页获取所有商品的API[GET]   /productList
@main.route('/productList', methods=['GET'])
def get_all_products():
    try:
        # 查询所有商品
        products = Product.query.all()

        # 将商品数据转换为字典列表
        product_list = []
        for product in products:
            category = Category.query.filter_by(catid=product.catid).first()

            product_data = {
                'productId': product.proid,
                'productName': product.name,
                'price': float(product.price),
                'description': product.description,
                'stock': product.stock,
                'createTime': product.createtime.strftime('%Y-%m-%d %H:%M:%S'),
                'updateTime': product.updatetime.strftime('%Y-%m-%d %H:%M:%S'),
                'category': category.name if category else 'N/A',  # 获取商品分类名
                'imageUrl': product.image,  # 返回图床 URL
                'sellerId': product.userid  # 添加商店信息
            }
            product_list.append(product_data)

        # 返回商品数据
        return jsonify({
            'status': 200,
            'message': '获取商品列表成功',
            'data': {
                'list': product_list
            }
        }), 200

    except Exception as e:
        # 捕获异常并返回错误信息
        return jsonify({
            'status': 500,
            'message': str(e),
        }), 500


# 买家获取某个商品的详细信息API[GET]   /detail
@main.route('/detail', methods=['GET'])
def get_product_detail():
    try:
        # 获取商品ID
        goods_id = request.args.get('goodsId')
        if not goods_id:
            return jsonify({
                "code": 0,
                "message": "Invalid input: Missing required field 'goodsId'"
            }), 400

        # 查询商品
        product = Product.query.filter_by(proid=goods_id).first()
        if not product:
            return jsonify({
                "code": 0,
                "message": f"Product not found with proid: {goods_id}"
            }), 404

        # 查询商品分类
        category = Category.query.filter_by(catid=product.catid).first()

        # 组装数据
        data = {
            "goods_id": product.proid,
            "goods_name": product.name,
            "price": str(product.price),  # 转换为字符串，前端显示时会自动转换回数字
            "stock": product.stock,
            "description": product.description,
            "category_id": product.catid,
            "category_name": category.catname,
            "image": product.image,
            "createtime": product.createtime.strftime("%Y-%m-%d %H:%M:%S"),
            "updatetime": product.updatetime.strftime("%Y-%m-%d %H:%M:%S")
        }

        return jsonify({
            "code": 200,
            "message": "Product detail retrieved successfully",
            "data": data
        }), 200

    except Exception as e:
        return jsonify({
            "code": 0,
            "message": str(e)
        }), 500  # 500 Internal Server Error


# 卖家修改商品API[PUT]   /seller_modify_product
@main.route('/seller_modify_product', methods=['PUT'])
@token_required
def modify_product(current_user):
    try:
        # Ensure the user is a seller
        if current_user.role != 'seller':
            return jsonify({
                "code": 0,
                "message": "Access denied: Only sellers can modify products"
            }), 403

        # Get the product ID and data from the request
        data = request.get_json()
        if not data or 'proid' not in data:  # or any other required fields
            return jsonify({
                "code": 0,
                "message": "Invalid input: Missing required field 'proid'"
            }), 400

        # Check if the product exists
        product = Product.query.filter_by(proid=data['proid']).first()
        if not product:
            return jsonify({
                "code": 0,
                "message": f"Product not found with proid: {data['proid']}"
            }), 404

        # Update the product data
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        product.description = data.get('description', product.description)
        product.image = data.get('image', product.image)
        product.stock = data.get('stock', product.stock)
        db.session.commit()

        return jsonify({
            "code": 200,
            "message": "Product modified successfully",
            "data": {
                "proid": data['proid']
            }
        }), 200  # OK

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "code": 0,
            "message": f"Error: {str(e)}"
        }), 500  # Internal Server Error


# 获取所有商品类别API[GET]   /category
@main.route('/category', methods=['GET'])
def get_all_categories():
    try:
        # 查询所有商品类别
        categories = Category.query.all()

        # 将商品类别数据转换为字典列表
        category_list = []
        for category in categories:
            category_data = {
                'categoryId': category.catid,
                'categoryName': category.name,
                'createTime': category.createtime.strftime('%Y-%m-%d %H:%M:%S'),
                'updateTime': category.updatetime.strftime('%Y-%m-%d %H:%M:%S')
            }
            category_list.append(category_data)

        # 返回商品类别数据
        return jsonify({
            'code': 200,
            'message': '获取商品类别列表成功',
            'data': {
                'categories': category_list
            }
        }), 200  # OK

    except Exception as e:
        # 捕获异常并返回错误信息
        return jsonify({
            'code': 500,
            'message': f"Error: {str(e)}"
        }), 500  # Internal Server Error
