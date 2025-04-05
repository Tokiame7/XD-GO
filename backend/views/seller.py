from flask import Blueprint, request, jsonify
from backend.models import db, Product, Category, Order, OrderItem
from backend.views.auth import token_required
import uuid

main = Blueprint('seller', __name__)


# 卖家获取店铺商品列表API[GET]   /getProduct
@main.route('/getProduct', methods=['GET'])
@token_required
def get_product(current_user):
    try:
        # 获取查询参数
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('pageSize', 10))
        search = request.args.get('search')

        # 使用当前卖家的userid来过滤商品
        seller_id = current_user.userid

    except ValueError:
        return jsonify({"code": 400, "message": "参数格式错误"}), 400

    query = Product.query.filter_by(userid=seller_id)

    # 如果提供了搜索条件，则按商品名或描述进行模糊搜索
    if search:
        query = query.filter(
            Product.name.ilike(f'%{search}%') |
            Product.description.ilike(f'%{search}%')
        )

    total = query.count()

    # 获取分页数据
    products = query.order_by(Product.createtime.desc()) \
        .offset((page - 1) * page_size) \
        .limit(page_size) \
        .all()

    # 构建返回数据
    data = []
    for product in products:
        # 获取商品分类
        category = Category.query.filter_by(catid=product.catid).first()

        product_data = {
            "productId": product.proid,
            "productName": product.name,
            "description": product.description,
            "price": float(product.price),
            "stock": product.stock,
            "createTime": product.createtime.strftime('%Y-%m-%d %H:%M:%S'),
            "updateTime": product.updatetime.strftime('%Y-%m-%d %H:%M:%S'),
            "category": category.name if category else 'N/A',  # 获取商品分类名
            "imageUrl": product.image,  # 返回图床 URL
            "catid": product.catid,
            "sellerId": product.userid,  # 添加商店信息
        }
        data.append(product_data)

    response = {
        "code": 200,
        "message": "获取商品列表成功",
        "data": data,
        "pagination": {
            "total": total,
            "page": page,
            "pageSize": page_size
        }
    }
    return jsonify(response), 200


# 卖家获取商品详情API[GET]   /seller_detail
@main.route('/seller_detail', methods=['GET'])
def seller_product_detail():
    goods_id = request.args.get('goodsId')

    if not goods_id:
        return jsonify({"status": 1, "message": "商品ID不能为空", "data": {}})

    product = Product.query.filter_by(proid=goods_id).first()

    if not product:
        return jsonify({"status": 1, "message": "商品不存在", "data": {}})

    seller = User.query.filter_by(userid=product.userid).first()

    data = {
        "goods_id": product.proid,
        "goods_name": product.name,
        "price": str(product.price),
        "stock": product.stock,
        "description": product.description,
        "category_id": product.catid,
        "image": product.image,
        "seller_info": {
            "seller_id": seller.userid,
            "seller_name": seller.username,
            "contact": seller.phone
        },
        "createtime": product.createtime.strftime("%Y-%m-%d %H:%M:%S"),
        "updatetime": product.updatetime.strftime("%Y-%m-%d %H:%M:%S")
    }

    return jsonify({"status": 0, "message": "成功", "data": {"detail": data}})


# 卖家更新自己的商品列表API[POST]   /updateProduct
@main.route('/updateProduct', methods=['POST'])
@token_required
def update_products(current_user):
    try:
        # 获取请求数据
        data = request.get_json()

        # 验证必要字段
        if not data or 'products' not in data:
            return jsonify({
                "code": 400,
                "message": "Invalid input: Missing required fields"
            }), 400

        products = data.get('products', [])

        # 验证每个商品数据
        for product_data in products:
            if not all(k in product_data for k in ['proid', 'price', 'stock']):
                return jsonify({
                    "code": 400,
                    "message": "Invalid product data: Missing required fields (proid, price or stock)"
                }), 400

            # 检查价格和库存是否为有效值
            if product_data['price'] <= 0 or product_data['stock'] < 0:
                return jsonify({
                    "code": 400,
                    "message": f"Invalid product data: Price must be positive "
                               f"and stock must be non-negative (proid: {product_data['proid']}) "
                }), 400

        # 批量更新商品
        for product_data in products:
            product = Product.query.filter_by(
                proid=product_data['proid'],
                userid=current_user.userid  # 确保商品属于当前卖家
            ).first()

            if not product:
                return jsonify({
                    "code": 404,
                    "message": f"Product not found or not owned by you (proid: {product_data['proid']})"
                }), 404

            # 更新商品信息
            if 'name' in product_data:
                product.name = product_data['name']
            if 'price' in product_data:
                product.price = product_data['price']
            if 'stock' in product_data:
                product.stock = product_data['stock']
            if 'description' in product_data:
                product.description = product_data['description']
            if 'catid' in product_data:
                # 验证分类是否存在
                category = Category.query.get(product_data['catid'])
                if not category:
                    return jsonify({
                        "code": 404,
                        "message": f"Category not found (catid: {product_data['catid']})"
                    }), 404
                product.catid = product_data['catid']

        # 提交数据库更改
        db.session.commit()

        return jsonify({
            "code": 200,
            "message": "Products updated successfully",
            "data": {
                "updated_count": len(products)
            }
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "code": 0,
            "message": str(e)
        }), 400


# 卖家增加自己的商品API[POST]   /addProduct
@main.route('/addProduct', methods=['POST'])
@token_required
def add_product(current_user):
    try:
        # 1. 获取并验证请求数据
        data = request.get_json()
        if not data:
            return jsonify({
                "code": 0,
                "message": "Invalid input: No JSON data provided"
            }), 400

        # 2. 验证必填字段
        required_fields = ['name', 'price', 'stock', 'catid']
        if not all(field in data for field in required_fields):
            return jsonify({
                "code": 0,
                "message": f"Missing required fields: {', '.join(required_fields)}"
            }), 400

        # 3. 验证数值有效性
        if data['price'] <= 0 or data['stock'] < 0:
            return jsonify({
                "code": 0,
                "message": "Price must be positive and stock must be non-negative"
            }), 400

        # 4. 验证分类是否存在
        category = Category.query.get(data['catid'])
        if not category:
            return jsonify({
                "code": 0,
                "message": f"Category not found: {data['catid']}"
            }), 404

        # 5. 检查商品名称是否重复（同一卖家的商品不允许重名）
        existing_product = Product.query.filter_by(
            name=data['name'],
            userid=current_user.userid  # 只检查当前卖家的商品
        ).first()

        if existing_product:
            return jsonify({
                "code": 0,
                "message": f"Product name '{data['name']}' already exists for your shop"
            }), 409  # HTTP 409 Conflict

        # 6. 创建新商品
        new_product = Product(
            proid=str(uuid.uuid4()),
            name=data['name'],
            price=data['price'],
            stock=data['stock'],
            description=data.get('description', ''),
            catid=data['catid'],
            userid=current_user.userid,
            image=data.get('image', '')
        )

        db.session.add(new_product)
        db.session.commit()

        # 7. 返回成功响应
        return jsonify({
            "code": 200,
            "message": "Product added successfully",
            "data": {
                "proid": new_product.proid,
                "name": new_product.name,
                "price": float(new_product.price)
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({
            "code": 500,
            "message": f"Server error: {str(e)}"
        }), 500


# 卖家删除自己的商品API[DELETE]   /deleteProduct
@main.route('/deleteProduct', methods=['DELETE'])
@token_required
def delete_product(current_user):
    try:
        # 1. 获取商品ID
        data = request.get_json()
        if not data or 'proid' not in data:
            return jsonify({
                "code": 0,
                "message": "Product ID (proid) is required"
            }), 400

        # 2. 检查商品是否存在
        product = Product.query.filter_by(proid=data['proid']).first()
        if not product:
            return jsonify({
                "code": 0,
                "message": f"Product not found with proid: {data['proid']}"
            }), 404

        # 3. 验证所有权
        if product.userid != current_user.userid:
            return jsonify({
                "code": 0,
                "message": f"No permission to delete product: {product.name} (proid: {data['proid']})"
            }), 403

        # 4. 记录待删除的商品名称（提交前获取）
        deleted_product_name = product.name

        # 5. 执行删除
        db.session.delete(product)
        db.session.commit()

        # 6. 返回成功响应（包含商品名称）
        return jsonify({
            "code": 200,
            "message": "Product deleted successfully",
            "data": {
                "deleted_proid": data['proid'],
                "deleted_name": deleted_product_name  # 新增返回字段
            }
        }), 200

    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({
            "code": 0,
            "message": f"Deletion failed: {str(e)}"
        }), 500


# 卖家获取所有订单列表API[GET]   /getList
@main.route('/list', methods=['GET'])
@token_required
def get_sell_order_list(current_user):
    try:
        # Ensure the user is a seller
        if current_user.role != 'seller':
            return jsonify({
                "code": 403,
                "message": "Access denied: Only sellers can view their orders"
            }), 403

        # Get the seller's orders
        orders = Order.query.filter_by(sellerid=current_user.userid).all()
        print(orders)
        if not orders:
            return jsonify({
                "code": 404,
                "message": "No orders found"
            }), 404

        # Get the order details for each order
        order_list = []
        for order in orders:
            order_items = OrderItem.query.filter_by(orderid=order.orderid).all()
            order_items_data = []
            for item in order_items:
                product = Product.query.filter_by(proid=item.proid).first()
                if not product:
                    return jsonify({
                        "code": 404,
                        "message": f"Product not found: {item.proid}"
                    }), 404

                order_items_data.append({
                    "proid": product.proid,
                    "name": product.name,
                    "price": str(product.price),
                    "quantity": item.quantity,
                    "image": product.image
                })

            order_list.append({
                "orderid": order.orderid,
                "totalprice": str(order.totalprice),
                "status": order.status,
                "createtime": order.createtime.strftime("%Y-%m-%d %H:%M:%S"),
                "order_items": order_items_data
            })

        # Return the order list
        return jsonify({
            "code": 200,
            "message": "Order list retrieved successfully",
            "data": {
                "orders": order_list
            }
        }), 200  # OK

    except Exception as e:
        print(e)
        return jsonify({
            "code": 500,
            "message": f"Error: {str(e)}"
        }), 500  # Internal Server Error


# 卖家修改订单状态[PUT]   /updateStatus
@main.route('/updateStatus', methods=['PUT'])
@token_required
def update_order_status(current_user):
    try:
        # Ensure the user is a seller
        if current_user.role != 'seller':
            return jsonify({
                "code": 403,
                "message": "Access denied: Only sellers can update order status"
            }), 403

        # Get the order ID and status from the request
        data = request.get_json()
        if not data or 'orderid' not in data or 'status' not in data:
            return jsonify({
                "code": 400,
                "message": "Invalid input: Missing required fields 'orderid' and'status'"
            }), 400

        # Check if the order exists
        order = Order.query.filter_by(orderid=data['orderid']).first()
        if not order:
            return jsonify({
                "code": 404,
                "message": f"Order not found with orderid: {data['orderid']}"
            }), 404

        # Check if the status is valid
        if data['status'] not in ['pending', 'delivered', 'shipped']:
            return jsonify({
                "code": 400,
                "message": f"Invalid status: {data['status']}"
            }), 400
        if data['status'] == 'pending' and order.status not in ['shipped', 'delivered']:
            data['status'] = 'shipped'
            # Update the order status
            order.status = data['status']
            db.session.commit()

            return jsonify({
                "code": 200,
                "message": "Order status updated successfully",
                "data": {
                    "orderid": data['orderid'],
                    "status": data['status']
                }
            }), 200  # OK

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "code": 500,
            "message": f"Error: {str(e)}"
        }), 500  # Internal Server Error
