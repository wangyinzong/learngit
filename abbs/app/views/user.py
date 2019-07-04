from flask import Blueprint, render_template, request, flash, get_flashed_messages
users = Blueprint('main', __name__)


@users.route('/register/', methods='GET', 'POST')
def register():
    return '我是用户 注册'
@users.route('/login/', methods='GET', 'POST')
def login():
    return '登录 wang666'
@users.route('/add_data/')
def add_data():
    return '增加'
@users.route('/delete_data/')
def delete_data():
    return '删除'
@users.route('/update_data/')
def update_data():
    return '修改'
@users.route('/select_data/')
def select_data():
    return '查找'