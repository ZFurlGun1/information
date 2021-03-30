from logging.handlers import RotatingFileHandler

from flask import Flask
# 可以用来指定SESSION的储存位置
import logging
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis

from config import config

# 初始化数据库
# 在falsk很多扩展里面都可以先初始化扩展对象，然后再去调用app_init方法初始化
db = SQLAlchemy()


def setup_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    """通过传入不同的配置名字，初始化其对应配置的应用实例"""
    # 配置日志,以便获取到指定配置所对应的日志等级
    setup_log(config_name)
    # 创建falsk对象
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config[config_name])

    db.init_app(app)
    # 初始化redis存储对象
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启当前csrf保护。只做服务器验证功能
    CSRFProtect(app)
    # 设置session保存指定位置
    Session(app)

    return app