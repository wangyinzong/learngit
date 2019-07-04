# encoding:utf-8
from flask import send_from_directory,Flask, request, render_template, url_for, session, flash, get_flashed_messages
from flask_script import Manager
from flask_bootstrap import Bootstrap
import os
from PIL import Image
# 设置允许上传文件类型
ALLOWED_EXTENSION = 'jpg'
# 创建实例
flask_a = Flask(__name__)
flask_a.config['SECRET_KEY'] = 'jiangxi'
flask_a.config['BOOTSTRAP_SERVE_LOCAL'] = True
manager = Manager(flask_a)
# 设置保存位置
flask_a.config['UPLOADED_FOLDER'] = os.getcwd()
# 上传文件大小限制
flask_a.config['MAX_CONTENT_LENGTH'] = 8*1024*1024
@flask_a.route('/uploads/', methods=['GET', 'POST'])
def uploads():
    img_url = ''
    if request.method == 'POST':
        file = request.files.get('photo')
        if file:
            #获取文件的后缀名
            suffix = os.path.splitext(file.filename)[1]
            # 生成随机文件名
            filename = random_string()+suffix
            # filename = file.filename
            # 当前路径+文件名
            pathname = os.path.join(flask_a.config['UPLOADED_FOLDER'])
            file.save(pathname)
            img = Image.open(pathname)
            img.thumbnail((128, 128))
            img.save(pathname)
    img_url = url_for('uploaded', filename=filename)
    return render_template('uploads.html', img_url=img_url)
@flask_a.route('/uploaded/<filename>/')
def uploaded(filename):
    return send_from_directory()

# 生成随机字符串
def random_string(length=16):
    import random
    base_dir = 'asddfghjklqwer12345678'
    return ''.join(random.choice(base_dir) for i in range(length))
# 判断允许类型
def allowde_file(filename):
    return '.' in filename and filename.rsplit('.', 1) in ALLOWED_EXTENSION
if __name__ == '__main__':
    flask_a.run(debug=True, threaded=True)