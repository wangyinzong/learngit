# encoding:utf-8
from flask import Flask, request, render_template, url_for, session, flash, get_flashed_messages
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
import os
# 导入表单基类
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from PIL import Image
# 创建实例
flask_a = Flask(__name__)
bootstrap = Bootstrap(flask_a)
flask_a.config['SECRET_KEY'] = 'wang'
# 设置保存位置
flask_a.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()
# 上传文件大小限制
flask_a.config['MAX_CONTENT_LENGTH'] = 8*1024*1024
# 上传文件类型
photos = UploadSet('photos', IMAGES)
flask_a.config['BOOTSTRAP_SERVE_LOCAL'] = True
configure_uploads(flask_a, photos)
# 设置上传大小，若为None，则为自定义为准
patch_request_class(flask_a, size=None)

# 上传文件表单类
class UploadForm(FlaskForm):
    photo = FileField('上传图像', validators=[FileRequired('文件未选择'), FileAllowed(photos, message="只能上传图片")])
    submit = SubmitField('立即上传')
# 生成随机字符串
def random_string(length=16):
    import random
    base_dir = 'asddfghjklqwer12345678'
    return ''.join(random.choice(base_dir) for i in range(length))

@flask_a.route('/uploads/', methods=['GET','POST'])
def uploads():
    img_url = ''
    # 如果提交方式是post，且文件已经提交
    form = UploadForm()
    if form.validate_on_submit():
        # 获取文件后缀
        suffix = os.path.splitext(form.photo.data.filename)[1]
        # 拼接文件名
        filename = random_string()+suffix
        # 保存文件
        photos.save(form.photo.data, name=filename)
        # 生成缩略图
        pathname = os.path.join(flask_a.config['UPLOADED_PHOTOS_DEST'], filename)
        # 打开图片
        img = Image.open(pathname)
        # 重新设置尺寸
        img.thumbnail((128, 128))
        # 保存图片
        img.save(pathname)
        # 获取路径
        img_url = photos.url(filename)
    return render_template('login.html', img_url=img_url, form=form)
if __name__ == '__main__':
    flask_a.run(debug=True, threaded=True)