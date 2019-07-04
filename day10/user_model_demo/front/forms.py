from django import forms
from django.contrib.auth import get_user_model
#get_user_model 导入用户模型  settings.py中设置了 AUTH_USER_MODEL = 'front.User' 就导入它

class LoginForm(forms.ModelForm):
    remember = forms.IntegerField(required=False)
    telephone = forms.CharField(max_length=11)
    class Meta:
        model = get_user_model()
        fields = ['password']