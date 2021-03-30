from info import redis_store
from . import index_blu


@index_blu.route('/')
def index():
    # session["name"] = "itheima"
    redis_store.set("name","itcast")

    return 'index'
