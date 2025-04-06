from flask import Blueprint, request, jsonify
from backend.models import User
from backend import db
import uuid
import jwt
import datetime
from backend.views.auth import token_required

main = Blueprint('user', __name__)


# 用户注册接口API[POST]   /register
@main.route('/register', methods=['POST'])
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


# 用户登录接口API[GET]   /login
@main.route('/login', methods=['GET'])
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
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)  # Token 有效期为 1 小时
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


# 买家/卖家获取用户个人信息API[GET]   /info
@main.route('/info', methods=['GET'])
@token_required
def get_user_info(current_user):
    try:
        # 根据用户角色返回不同的信息
        if current_user.role == 'buyer':
            user_info = {
                'userid': current_user.userid,
                'username': current_user.username,
                'email': current_user.email,
                'phone': current_user.phone,
                'role': current_user.role,
                'shipping_address': current_user.shipping_address
            }
        elif current_user.role == 'seller':
            user_info = {
                'userid': current_user.userid,
                'username': current_user.username,
                'email': current_user.email,
                'phone': current_user.phone,
                'role': current_user.role
            }
        else:
            return jsonify({
                "code": 400,
                "message": "Invalid user role"
            }), 400

        return jsonify({
            "code": 200,
            "message": "User info retrieved successfully",
            "data": user_info
        }), 200

    except Exception as e:
        return jsonify({
            "code": 500,
            "message": str(e)
        }), 500


# 买家修改用户个人地址API[PUT]   /address_edit
@main.route('/address_edit', methods=['PUT'])
@token_required
def update_shipping_address(current_user):
    try:
        # 验证用户角色
        if current_user.role != 'buyer':
            return jsonify({
                "code": 0,
                "message": "Access denied: Only buyers can update shipping address"
            }), 403

        # 获取请求数据
        data = request.get_json()
        if not data or 'shipping_address' not in data:
            return jsonify({
                "code": 0,
                "message": "Invalid input: Missing required field 'shipping_address'"
            }), 400

        # 更新收货地址
        current_user.shipping_address = data['shipping_address']
        db.session.commit()

        return jsonify({
            "code": 200,
            "message": "Shipping address updated successfully",
            "data": {
                "userid": current_user.userid,
                "username": current_user.username,
                "new_shipping_address": current_user.shipping_address
            }
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "code": 0,
            "message": str(e)
        }), 500


# 用户更改个人信息接口API[PUT]   /profile_edit
@main.route('/profile_edit', methods=['PUT'])
@token_required
def update_profile(current_user):
    try:
        # 获取请求数据
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        phone = data.get('phone')
        shipping_address = data.get('shipping_address')

        # 更新用户信息
        if username:
            current_user.username = username
        if email:
            current_user.email = email
        if phone:
            current_user.phone = phone
        if shipping_address:
            current_user.shipping_address = shipping_address

        # 提交到数据库
        db.session.commit()

        # 返回更新后的用户信息
        user_info = {
            'userid': current_user.userid,
            'username': current_user.username,
            'email': current_user.email,
            'phone': current_user.phone,
            'shipping_address': current_user.shipping_address
        }

        return jsonify({
            "code": 200,
            "message": "Profile updated successfully",
            "data": user_info
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "code": 0,
            "message": str(e)
        }), 500
