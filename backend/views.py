from flask import Blueprint, request, jsonify
from backend.models import *
from backend.models import Product
import uuid
import jwt
import datetime

main = Blueprint('main', __name__)


# 主界面
@main.route('/', methods=['GET'])
def index():
    return "Welcome to the XD_GO Home", 200


# 测试API
@main.route('/api/test', methods=['GET'])
def test():
    return "Welcome to the API Test", 200


# 测试从数据库读取数据的 API
@main.route('/api/users/get_users', methods=['GET'])
def get_users():
    try:
        # 查询所有用户
        users = User.query.all()

        # 将用户数据转换为字典列表
        user_list = []
        for user in users:
            user_data = {
                'userid': user.userid,
                'username': user.username,
                'email': user.email,
                'role': user.role
            }
            user_list.append(user_data)

        # 返回用户数据
        return {
                   'status': 'success',
                   'data': user_list
               }, 200

    except Exception as e:
        # 捕获异常并返回错误信息
        return {
                   'status': 'error',
                   'message': str(e)
               }, 500


# 获取店铺商品列表
@main.route('/api/sell_order/getProduct', methods=['GET'])
def get_product():
    try:
        # 获取查询参数
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('pageSize', 10))
        search = request.args.get('search')
        seller_id = request.args.get('sellerid')  # 新增的 sellerid 参数，用于过滤指定用户的商品

    except ValueError:
        return jsonify({"code": 400, "message": "参数格式错误"}), 400

    query = Product.query

    # 如果提供了店铺 ID，则过滤出该店铺的商品
    if seller_id:
        query = query.filter_by(shopid=seller_id)

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
    return jsonify(response)


# 用户注册接口
@main.route('/api/users/register', methods=['POST'])
def register_user():
    try:
        # 获取请求数据
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        phone = data.get('phone')
        role = data.get('role')

        # 验证输入参数
        if not username or not password or not email or not role:
            return jsonify({
                "code": 0,
                "message": "Invalid input: Missing required fields"
            }), 400

        # 验证角色是否合法
        if role not in ['buyer', 'seller', 'admin']:
            return jsonify({
                "code": 0,
                "message": "Invalid input: Role must be 'buyer', 'seller', or 'admin'"
            }), 400

        # 检查用户名是否已存在
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({
                "code": 0,
                "message": "Invalid input: Username already exists"
            }), 400

        # 创建新用户
        new_user = User(
            userid=str(uuid.uuid4()),  # 生成唯一的用户ID
            username=username,
            password=password,  # 注意：实际项目中密码应加密存储
            email=email,
            phone=phone,
            role=role
        )

        # 添加到数据库
        db.session.add(new_user)
        db.session.commit()

        # 返回注册成功信息
        return jsonify({
            "code": 200,
            "message": "User registered successfully",
            "data": {
                "userid": new_user.userid,
                "username": new_user.username,
                "role": new_user.role
            }
        }), 200

    except Exception as e:
        # 捕获异常并返回错误信息
        return jsonify({
            "code": 0,
            "message": str(e)
        }), 400


# 用户登录接口
@main.route('/api/users/login', methods=['GET'])
def login_user():
    try:
        # 获取查询参数
        username = request.args.get('username')
        password = request.args.get('password')

        # 验证输入参数
        if not username or not password:
            return jsonify({
                "code": 0,
                "message": "Invalid input: Missing required fields"
            }), 400

        # 查询用户
        user = User.query.filter_by(username=username, password=password).first()
        if not user:
            return jsonify({
                "code": 0,
                "message": "Invalid input: Incorrect username or password"
            }), 401

        # 生成 JWT Token
        token_payload = {
            'userid': user.userid,
            'username': user.username,
            'role': user.role,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token 有效期为 1 小时
        }
        token = jwt.encode(token_payload, 'your_secret_key', algorithm='HS256')  # 使用密钥和算法生成 Token

        # 返回登录成功信息
        return jsonify({
            "code": 200,
            "message": "Login successful",
            "data": {
                "userid": user.userid,
                "username": user.username,
                "role": user.role,
                "token": token  # 返回生成的 Token
            }
        }), 200

    except Exception as e:
        # 捕获异常并返回错误信息
        return jsonify({
            "code": 0,
            "message": str(e)
        }), 400


# 获取所有商品的API
@main.route('/api/product/productList', methods=['GET'])
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
