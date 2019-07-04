# encoding:utf-8

# 导入类库

from flask import Blueprint

# 创建蓝本对象  名字=mall
mall = Blueprint('mall', __name__)
@mall.route('/shopping/')
def shopping():
    return '小姐姐是呵呵'
@mall.route('/gouwuche/')
def gouwuche():
    return '小哥哥也是呵呵'
