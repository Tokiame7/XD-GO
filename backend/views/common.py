from flask import Blueprint
from backend.models import User

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
