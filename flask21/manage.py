# encoding:utf-8

# 导入类库
from flask import Flask, request, redirect, url_for, abort, make_response , session
import time
from flask_script import Manager
# 导入蓝本对象
from user import user
from mall import mall
# 创建实例
flask_a = Flask(__name__)
flask_a.config['SECRET_KEY'] = 'jxust'
# 实例化 manager对象
manager = Manager(flask_a)
# 创建视图函数 V
@flask_a.route('/')
def index():
    return '主页面'
@flask_a.route('/admin/')
def admin():
    return '江理大学管理系统后台'
@flask_a.route('/login/<name>/')    # 路由地址
# 参数传递到视图方法
def login(name):
    return '欢迎%s登录' % name
@flask_a.route('/register/<int:uid>/')
def register(uid):
    return '欢迎%s注册' % uid
@flask_a.route('/path/<path:p>/')
def path(p):
    return '欢迎%s注册' % p
@flask_a.route('/req/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def req():
    #return request.base_url       # 返回客户端请求完整的url ,不包含参数
    #return request.host_url       # 返回ip地址和端口号
    #return request.path           # 返回请求路径
    #return request.method         # 返回请求方法
    #return request.remote_addr    # 返回客户端的ip地址
    #return request.args['page']   # 返回客户端请求的get参数值
    return request.headers['User-Agent']     # 返回客户端请求的header 信息
@flask_a.route('/respon/')
def respon():
    return 'OK', 200           # 状态码默认200，可以自定义状态码如，404
@flask_a.route('/old1/')
def old1():
    #return redirect('/login/')
    return redirect(url_for('new'))
@flask_a.route('/old2/')
def old2():
    # return redirect('/login/')
    return redirect(url_for('new'))
@flask_a.route('/old3/')
def old3():
    # return redirect('/login/')
    return redirect(url_for('new'))   # url_for 根据视图方法 获取到对应的  路由地址  然后交给redirect
@flask_a.route('/login/')
def new():
    return '新,请先登录'
# 终止错误 抛异常
@flask_a.route('/aborts/')
def aborts():
    abort(404)          # 自定义抛错
    return 'just test'
# 自定义错误页面
@flask_a.errorhandler(404)
def page_not_found(e):
    return '看啥呢，滚！'
@flask_a.route('/set_cookie/')
def set_cookie():
    res = make_response('set_cookie')
    expire = time.time()+100  # 当前时间往后+100s有效
    res.set_cookie('name', 'kangbazi13', expires=expire)
    return res
@flask_a.route('/get_cookie/')
def get_cookie():
    return request.cookies.get('name') or 'cookie is not set'
@flask_a.route('/set_session/')
def set_session():
    session['username'] = 'kangbazi444'
    return 'session is set'
@flask_a.route('/get_session/')
def get_session():
    return session.get('username', 'who are you')
flask_a.register_blueprint(user, url_prefix='/user')
flask_a.register_blueprint(mall, url_prefix='/mall')
# 启动
if __name__ == '__main__':
    flask_a.run(debug=True,port=5077,threaded=True)  # port=指定端口号
    #manager.run()               # python manage.py runserver -d -r -p 5056 -h 0.0.0.0 --threaded