from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,Email
from wtforms.validators import ValidationError
from flask_wtf.file import FileField,FileRequired,FileAllowed
from app.models import User #自定义验证函数 用户提交检测数据中是否存在
from app.exts import photos #只能上传图片
#用户注册表单
class RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(6,20,message="用户名必须在6到20位之间")])
    email = StringField('Email',validators=[Email(message="邮箱格式不正确")])
    password =PasswordField('密码',validators=[DataRequired(),Length(6,20,message="密码长度必须在6到20位之间")])
    confirm = PasswordField('确认密码',validators=[EqualTo('password',message="两次密码不一致")])
    submit = SubmitField('立即注册')

    def validate_username(self,filed):
        if User.query.filter_by(username=filed.data).first():
            raise ValidationError("该用户已经注册请选择其它用户")

    def validate_email(self, filed):
        if User.query.filter_by(email=filed.data).first():
            raise ValidationError("该邮箱已经被占用请用其它邮箱")

#用户登录表单
class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(6,20,message="用户名必须在6到20位之间")])
    password =PasswordField('密码',validators=[DataRequired(),Length(6,20,message="密码长度必须在6到20位之间")])
    remember = BooleanField('记住我')
    submit = SubmitField('立即登录')
#用户上传表单
class UploadForm(FlaskForm):
    icon = FileField("头像",validators=[FileRequired(),FileAllowed(photos,message="只能上传图片类型")])
    submit = SubmitField('立即上传')
# 修改密码表单
class Change_passwordForm(FlaskForm):
    old_password = StringField('旧密码',validators=[DataRequired(),Length(6,20,message="密码长度必须在6到20位之间")])
    new_password = StringField('新密码',validators=[DataRequired(),Length(6,20,message="新密码必须在6到20位之间")])
    confirm = PasswordField('确认新密码', validators=[EqualTo('new_password', message="两次密码不一致")])
    submit = SubmitField('确定修改')
# 找回密码表单
class Retrieve_passwordForm(FlaskForm):
    mail = StringField('Email',validators=[Email(message="邮箱格式不正确")])
    submit = SubmitField('确定')
class Retrieve_pwdForm(FlaskForm):
    new_password = StringField('新密码',validators=[DataRequired(),Length(6,20,message="新密码必须在6到20位之间")])
    confirm = PasswordField('确认新密码', validators=[EqualTo('new_password', message="两次密码不一致")])
    submit = SubmitField('确定')
#修改邮箱表单
class Change_mailForm(FlaskForm):
    new_mail = StringField('新Email', validators=[Email(message="邮箱格式不正确")])
    submit = SubmitField('确定')