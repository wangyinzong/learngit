from .models import User
from django import forms


class SignUpForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=30,min_length=6)
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError("密码不一致")
        return cleaned_data
    class Meta:
        model = User
        fields = '__all__'

class SignInForm(forms.ModelForm):
    def get_errors(self):
        new_errors = []
        errors = self.errors.get_json_data()
        for messages in errors.values():
            for message_dict in messages:
                for key,message in message_dict.items():
                    if key == "message":
                        new_errors.append(message)
        return new_errors
    class Meta:
        model = User
        fields = ['username','password']

        error_messages = {
            'username':{
                'min_length':'用户名至少6位',
            },
            'password':{
                'min_length':'密码至少6位',
            }
        }
