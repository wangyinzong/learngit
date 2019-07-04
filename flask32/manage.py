# encoding:utf-8
from flask import Flask, render_template, request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
# 导入表单类型
from wtforms import StringField, SubmitField, PasswordField
# 导入表单验证
from wtforms.validators import DataRequired
# 创建实例
flask_b = Flask(__name__)
bootstrap = Bootstrap(flask_b)
manager = Manager(flask_b)
flask_b.config['SECRET_KEY'] = '江西理工大学'
# 编写表单类
class NameForm(FlaskForm):
    name = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码')
    submit = SubmitField('立即登陆')

# 视图函数
@flask_b.route('/')
def feet():
    return "Hello ！"
@flask_b.route('/login/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    else:
        return "hello %s !! 您的密码是 %s !" % (request.form['username'], request.form['password'])
# 启动

if __name__ == '__main__':
    flask_b.run(debug=True, port=5060,threaded=True)
    # manager.run()