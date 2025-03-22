from flask import Blueprint

main = Blueprint('main', __name__)


# 主界面
@main.route('/', methods=['GET'])
def index():
    return "Welcome to the API Home", 200


# 测试API
@main.route('/test', methods=['GET'])
def test():
    return "Welcome to the API Test", 200
