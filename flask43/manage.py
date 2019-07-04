# encoding:utf-8
from flask import Flask, request, render_template, url_for, session, flash, get_flashed_messages
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
import os
from PIL import Image
# 创建实例
flask_a = Flask(__name__)
flask_a.config['SECRET_KEY'] = 'jiangxi'
# 设置保存位置
flask_a.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()
# 上传文件大小限制
flask_a.config['MAX_CONTENT_LENGTH'] = 8*1024*1024
# 上传文件类型
photos = UploadSet('photos', IMAGES)

configure_uploads(flask_a, photos)
# 设置上传大小，若为None，则为自定义为准
patch_request_class(flask_a, size=None)

@flask_a.route('/uploads/', methods=['GET','POST'])
def uploads():
    img_url = ''
    # 如果提交方式是post，且文件已经提交
    if request.method == 'POST' and 'images' in request.files:
        # 保存文件
        filename = photos.save(request.files['images'])
        # 获取图片url
        img_url = photos.url(filename)
    return render_template('login.html', img_url=img_url)
if __name__ == '__main__':
    flask_a.run(debug=True, threaded=True)