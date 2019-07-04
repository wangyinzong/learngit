import os
from flask import Blueprint,render_template,url_for,request,flash,get_flashed_messages,redirect,current_app
from app.forms import RegisterForm,LoginForm,UploadForm,Change_mailForm,Change_passwordForm,Retrieve_passwordForm,Retrieve_pwdForm
from app.models import User
from app.exts import db,photos
from app.email import send_mail
from flask_login import login_required,login_user,logout_user,current_user
from PIL import Image
users = Blueprint('users',__name__)

name = ''
@users.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        u = User(username=form.username.data,password=form.password.data,email=form.email.data)
        db.session.add(u)
        db.session.commit()

        #生成token  用u对象调用模型中的方法
        token = u.generate_active_token()
        send_mail(u.email,'账户激活','email/activate',username=u.username,token=token)
        flash("恭喜注册成功,请点击邮件中的链接完成激活")
        return redirect(url_for('users.login'))
    return render_template('user/register.html',form=form)



#这个方法用来验证token  给用户邮箱发送过去一个完整的url
@users.route('/active/<token>/',methods=['GET','POST'])
def active(token):
    if User.check_active_token(token):


        flash("账户激活成功")
        return render_template(url_for('users.login'))
    else:
        flash("账户激活失败")
        return redirect(url_for('main.index'))
#这个方法用来验证token  给用户邮箱发送过去一个完整的url
@users.route('/active_mail/<token>/',methods=['GET','POST'])
def active_mail(token):
    username = request.args.get('username', 1, type=str)
    if User.check_active_token(token):
        flash("验证完成修改成功")
        return redirect(url_for('users.retrieve_pwd',username=username))
    else:
        flash("邮箱激活失败")
        return redirect(url_for('main.index'))

@users.route('/login/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if not u:
            flash("该用户名不存在")
        elif not u.confirmed:
            flash("该账户没有激活,请激活后登录")
        elif u.verify_password(form.password.data):
            login_user(u,remember=form.remember.data)
            flash("登录成功")
            return redirect( request.args.get('next') or url_for("main.index"))
        else:
            flash("密码不正确")
    return render_template('user/login.html',form=form)

@users.route('/logout/',methods=['GET','POST'])
def logout():
    logout_user()
    flash("退出登录成功")
    return redirect(url_for('main.index'))

@users.route('/test/',methods=['GET','POST'])
@login_required
def test():
    return 'this is test'

@users.route('/change_password/',methods=['GET', 'POST'])
@login_required
def change_password():
    form = Change_passwordForm()
    if form.validate_on_submit():
        old_password = form.old_password.data
        u = current_user
        if u.verify_password(old_password):
            new_password = form.new_password.data
            u.password = new_password
            db.session.add(u)
            logout_user()
            flash("修改成功！请重新登录!")
            return redirect(url_for('main.index'))
        else:
            flash("请输入正确的密码！")
    return render_template('user/change_password.html',form=form)
@users.route('/change_mail/', methods=['GET', 'POST'])
def change_mail():
    form = Change_mailForm()
    if form.validate_on_submit():
        u = current_user
        new_mail = form.new_mail.data
        u.mail = new_mail
        db.session.add(u)
        flash("邮箱修改成功")
        return redirect(url_for('main.index'))
    return render_template('user/change_mail.html',form=form)
@users.route('/retrieve_pwd/',methods=['GET','POST'])
def retrieve_pwd():
    username = request.args.get('username', 1, type=str)
    form = Retrieve_pwdForm()
    if form.validate_on_submit():
        password = form.new_password.data
        u = User.query.filter_by(username=username).first()
        u.password = password
        db.session.add(u)
        flash("密码重置成功，请再次登录！")
        return redirect(url_for('main.index'))
    return render_template('user/retrieve_pwd.html',form=form)
@users.route('/retrieve_password/',methods=['GET', 'POST'])
def retrieve_password():
    form = Retrieve_passwordForm()
    if form.validate_on_submit():
        mail = form.mail.data
        u = User.query.filter_by(email=mail).first()
        if u:
            token = u.generate_active_token()
            send_mail(u.email, '找回密码', 'email/retrieve_pwd', username=u.username, token=token)
            flash("恭喜修改成功")
        else:
            flash("请输入正确邮箱")
    return render_template('user/retrieve_password.html', form=form)
@users.route('/change_icon/',methods=['GET','POST'])
@login_required
def change_icon():
    img_url = ''
    form = UploadForm()
    if form.validate_on_submit():
        #获取文件后缀
        suffix = os.path.splitext(form.icon.data.filename)[1]
        #随机文件名  拼接
        filename = random_string()+suffix
        photos.save(form.icon.data,name=filename)
        pathname = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],filename)
        img = Image.open(pathname)
        img.thumbnail((128,128))
        img.save(pathname)
        if current_user.icon != 'default.jpg':
            os.remove(current_app.config['UPLOADED_PHOTOS_DEST'],current_user.icon)
        current_user.icon = filename #将新上传的文件名 赋值给 用户的头像
        db.session.add(current_user)#保存在数据库中
        flash("头像上传成功")
        return redirect(url_for("users.change_icon"))
    img_url = photos.url(current_user.icon)
    return render_template('user/change_icon.html',form=form,img_url=img_url)

def random_string(length=20):
    import random
    base_str = 'abc123defhijklmnopqrstuvwxyz4567890'
    return ''.join(random.choice(base_str) for i in range(length))