from flask import Blueprint, request, jsonify
import jwt
from functools import wraps
from backend.models import User

main = Blueprint('auth', __name__)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token_parts = auth_header.split(' ')
            if len(token_parts) == 2 and token_parts[0] == 'Bearer':
                token = token_parts[1]

        if not token:
            return jsonify({"code": 0, "message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
            current_user = User.query.filter_by(userid=data['userid']).first()
            if not current_user:
                raise Exception("User not found")
        except jwt.ExpiredSignatureError:
            return jsonify({"code": 0, "message": "Token expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"code": 0, "message": "Invalid token!"}), 401
        except Exception as e:
            return jsonify({"code": 0, "message": str(e)}), 401

        return f(current_user, *args, **kwargs)

    return decorated
