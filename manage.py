from flask import Flask, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
# 可以用来指定session保存的位置
from flask_session import Session
from config import Config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db

app = create_app('developement')
manager = Manager(app)

# 数据库迁移
#将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session["name"] = "itheima"
    return 'index'


if __name__ == '__main__':
    manager.run()
