from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db


# create_app类似于工厂方法
app = create_app('development')
manager = Manager(app)

# 数据库迁移
#将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)




if __name__ == '__main__':
    manager.run()
