from . import index_blu


@index_blu.route('/')
def index():
    # session["name"] = "itheima"
    return 'index'
