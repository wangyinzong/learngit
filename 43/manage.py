# encoding:utf-8
from flask import Flask, request, render_template, url_for, session, flash, get_flashed_messages
from flask_script import Manager
# 导入表单类库
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, email, length, EqualTo
from flask_moment import Moment
from datetime import datetime, timedelta
# 创建实例
flask_a = Flask(__name__)
flask_a.config['SECRET_KEY'] = 'jiangxi'
flask_a.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(flask_a)
manager = Manager(flask_a)
moment = Moment(flask_a)
class TestForm(FlaskForm):
    name = StringField('用户名', validators=[DataRequired(), length(min=6, max=12)])
    email = StringField('邮箱', validators=[email()])
    password = PasswordField('密码', validators=[DataRequired(),length(min=6, max=32), EqualTo('confirm')])
    confirm = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('立即登录')
@flask_a.route('/uploads/',methods=['GET', 'POST'])
def uploads():
    form = TestForm()
    # if request.method == 'POST':
    #     #session['name'] = request.form['name']
    #     session['name'] = form.name.data
    #     session['email'] = form.email.data
    # name = session.get('name')
    # email = session.get('email')
    # 表单校验
    if form.validate_on_submit():
        last_name = session.get('name')
        if last_name and last_name != form.name.data:
            flash('用户名别换！')
            flash('你是睿智吗！')
            flash('别皮！')
        session['name'] = form.name.data
        session['email'] = form.email.data
    name = session.get('name')
    email = session.get('email')
    return render_template('login.html', form=form, name=name, email=email)
@flask_a.route('/moments/')
def moments():
    current_time = datetime.utcnow()+timedelta(seconds=-50)
    return render_template('moments.html', current_time=current_time)
if __name__ == '__main__':
    flask_a.run(debug=True, threaded=True)