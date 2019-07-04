# encoding:utf-8

# 导入类库

from flask import Blueprint

# 创建蓝本对象  名字=user
user = Blueprint('user', __name__)

@user.route('/login/<name>/')    # 路由地址
# 参数传递到视图方法
def login(name):
    return '欢迎%s登录' % name
@user.route('/register/<int:uid>/')
def register(uid):
    return '欢迎%s注册' % uid