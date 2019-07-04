from django import forms
from django.core import validators
from front.models import User

class BaseForm(forms.Form):
    def get_errors(self):
        # {'telephone':[{'message':'1344444:已注册',}]}
        errors = self.errors.get_json_data()
        new_errors = {}
        for key,message_dicts in errors.items():
            messages = []
            # print(message_dicts)
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors
class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=100,min_length=6,label="标题",error_messages={"min_length":"不能少于6个字"})
    content = forms.CharField(widget=forms.Textarea,label="内容",error_messages={"required":"必填"})
    email = forms.EmailField(label="邮箱",error_messages={"required":"必填"})
    reply = forms.BooleanField(required=False,label="是否回复")
class RegisterForm(BaseForm.Form):
    username = forms.CharField(max_length=100)
    email = forms.CharField(validators=[validators.EmailValidator(message="请输入正确格式邮箱")])
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[34578]\d{9}',message="请输入正确格式号码")])
    pwd1 = forms.CharField(max_length=20,min_length=6)
    pwd2 = forms.CharField(max_length=20,min_length=6)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message="%s:已注册"%telephone)
        return telephone
    # 如果走到这里说明所有的字段都验证成功了
    def clean(self):# 系统方法
        clean_data = super(RegisterForm,self).clean()
        pwd1 = clean_data.get('pwd1')
        pwd2 = clean_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message="密码不一致")
        return clean_data
