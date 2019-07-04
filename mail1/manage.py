from flask import Flask, render_template, current_app
from flask_script import Manager
from flask_mail import Mail, Message
import os
from threading import Thread

flask_a = Flask(__name__)

manager = Manager(flask_a)

flask_a.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER',
                                               'smtp.163.com')
flask_a.config['MAIL_USERNAME'] = os.environ.get('MAIL_SERVER',
                                                 '15179809270@163.com')
flask_a.config['MAIL_PASSWORD'] = os.environ.get('MAIL_SERVER',
                                                 'wangyinzong')
# mail对象之前完成邮箱服务器配置 用户密码配置
mail = Mail(flask_a)

# 封装发送邮件函数
def send_mail(subject,to, template, **kwargs):
    # 创建邮件发送对象
    msg = Message(subject=subject, recipients=to,
                  sender=flask_a.config['MAIL_USERNAME'])
    msg.html = render_template(template+'.html', **kwargs)
    msg.body = render_template(template+'.txt', **kwargs)
    mail.send(message=msg)
def async_send_mail(app, msg):
    with app.app_context():
        mail.send(message=msg)
def send_to_mail(subject, to, template, **kwargs):
    # 根据current_app 获取到 当前 应用实例
    app = current_app._get_current_object()
    # 创建邮件对象
    msg = Message(subject=subject, recipients=to,
                  sender=app.config['MAIL_USERNAME'])
    # 显示邮件内容
    msg.html = render_template(template+'.html', **kwargs)
    msg.body = render_template(template+'.txt', **kwargs)
    # 创建线程
    thr = Thread(target=async_send_mail, args=[app, msg])
    # 启动线程
    thr.start()
    return thr
@flask_a.route('/')
def index():
    # 创建邮件发送对象
    # msg = Message(subject='账号激活', recipients=['751925571@qq.com', '1370818974@qq.com'],
    #                   sender=flask_a.config['MAIL_USERNAME'])
    # msg.html = render_template('activate.html',
    #                            username='wangyinzong')
    # msg.body = render_template('activate.txt',
    #                            username='wangyinzong')
    # mail.send(message=msg)
    send_to_mail('我！！', ['1370818974@qq.com', '863528368@qq.com'],
                 'activate', username='银圣')
    return '邮件已发送！'
if __name__ == '__main__':
    flask_a.run(debug=True, threaded=True, port=5060)

