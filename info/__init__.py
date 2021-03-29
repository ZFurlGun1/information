from flask import Flask
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis


from config import Config

# 初始化数据库
db = SQLAlchemy()


def create_app(config_name):
    """通过传入不同的配置名字，初始化其对应配置的应用实例"""
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(Config)

    db.init_app(app)
    # 初始化redis存储对象
    redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
    # 开启当前csrf保护。只做服务器验证功能
    CSRFProtect(app)
    #设置session保存指定位置
    Session(app)

    return app
