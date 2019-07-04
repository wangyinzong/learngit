from django import forms
from .models import Book, User


class AddBookForm(forms.ModelForm):
    # 此处省略三个字段

    class Meta:
        model = Book
        # fields = "__all__" # 应用所有字段
        # fields = ['title','page'] # 应用title,page 字段
        exclude = ['price']  # 除了该字段，模型字段全用
        error_messages = {
            'page': {
                'required': '请传入page参数',
                'invalid': '请传入可用的page参数'
            },
            'title': {
                'max_length': '最大长度为100'
            },
            'price': {
                'max_value': '不能超过1000元'
            }
        }


class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pwd1 = self.cleaned_data.get('pwd1')
        pwd2 = self.cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message="密码输入不一致")
        return cleaned_data

    class Meta:
        model = User
        exclude = ['password']
