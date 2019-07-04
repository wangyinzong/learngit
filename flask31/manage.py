# encoding:utf-8
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
# 创建实例
flask_b = Flask(__name__)
bootstrap = Bootstrap(flask_b)
manager = Manager(flask_b)

# 视图函数
@flask_b.route('/')
def index():
    context = {
        'username': '名字',
        'age': 15,
        'country': 'china',
        'scripts': '<script>alert("这是一个提示脚本")</script>',
        'childrens': {
            'name': 'test',
            'height': '233cm'
        }
    }
    return render_template('index.html', **context)
@flask_b.route('/statics/')
def statics():
    return render_template('static.html')
@flask_b.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
# 启动

if __name__ == '__main__':
    flask_b.run(debug=True, threaded=True)
    # manager.run()