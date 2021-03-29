from redis import StrictRedis


class Config(object):
    """项目的配置"""

    DEBUG = True

    SECRET_KEY = "jobUtRvVM5V5ArvQLbjmFwdVf20jcvdtE0kmT7Ef61ngxa0YNTt/kMVJ1YEplMUv"

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 为redisde 的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session保存配置
    SESSION_TYPE = "redis"
    # 开启session的签名
    SESSION_USE_SIGNER = True
    # 指定session保存的redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


class DevelopementConfig(Config):
    """开发模式下的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产模式下的配置"""
    pass


# 定义配置字典
config = {
    "development": DevelopementConfig,
    "production": ProductionConfig
}
