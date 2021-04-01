from flask import current_app
from flask import render_template

from info import redis_store
from . import index_blu


# @index_blu.route('/')
# def index():
#     # 向redis中保存一个值 name itcast
#     redis_store.set("name", "itcast")
#     return 'index'


@index_blu.route('/')
def index():
    return render_template('news/index.html')


@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')
