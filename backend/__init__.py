from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import DevelopmentConfig  # 引入配置文件

# 初始化数据库对象
db = SQLAlchemy()

# 初始化迁移对象
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    CORS(app)  # 启用跨域请求
    app.config.from_object(DevelopmentConfig)  # 加载配置

    # 初始化数据库和迁移
    db.init_app(app)
    migrate.init_app(app, db)

    # 注册蓝图
    from backend.views import main
    app.register_blueprint(main)

    return app
