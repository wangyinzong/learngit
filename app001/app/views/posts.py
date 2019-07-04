from flask import Blueprint,render_template,url_for,request,flash,get_flashed_messages,redirect,jsonify
from flask_login import current_user
posts = Blueprint('posts',__name__)


#用户点击 收藏 取消收藏 用这个来处理
@posts.route('/collect/<int:pid>/')
def collect(pid):
    if current_user.is_favorite(pid):
        current_user.del_favorite(pid)
    else:
        current_user.add_favorite(pid)
    return jsonify({'result':'ok'})