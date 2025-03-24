from flask import Blueprint, request, jsonify
from backend.models import *
from backend.models import Product
import uuid

main = Blueprint('main', __name__)


# 主界面
@main.route('/', methods=['GET'])
def index():
    return "Welcome to the API Home", 200


# 测试API
@main.route('/test', methods=['GET'])
def test():
    return "Welcome to the API Test", 200


# 测试从数据库读取数据的 API
@main.route('/get_users', methods=['GET'])
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

# 获取商品列表
@main.route('/api/sell_order/getProduct', methods=['GET'])
def get_product():
    try:
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('pageSize', 10))
        search = request.args.get('search')
    except ValueError:
        return jsonify({"code": 400, "message": "参数格式错误"}), 400

    query = Product.query  # ➡️ 已删除 `Product.status` 的引用

    if search:
        query = query.filter(
            Product.name.ilike(f'%{search}%') |
            Product.description.ilike(f'%{search}%')
        )

    total = query.count()

    products = query.order_by(Product.createtime.desc()) \
                    .offset((page - 1) * page_size) \
                    .limit(page_size) \
                    .all()

    data = [{
        "productId": product.proid,
        "productName": product.name,
        "description": product.description,
        "price": float(product.price),
        "stock": product.stock,
        "imageUrl": f"http://example.com/images/{product.proid}.jpg",
        "createTime": product.createtime.strftime('%Y-%m-%d %H:%M:%S'),
        "updateTime": product.updatetime.strftime('%Y-%m-%d %H:%M:%S'),
        "catid": product.catid
    } for product in products]

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

        # 返回登录成功信息
        return jsonify({
            "code": 200,
            "message": "Login successful",
            "data": {
                "userid": user.userid,
                "username": user.username,
                "role": user.role
            }
        }), 200

    except Exception as e:
        # 捕获异常并返回错误信息
        return jsonify({
            "code": 0,
            "message": str(e)
        }), 400

# 测试gitkraken功能，本行注释没有任何实际意义！
