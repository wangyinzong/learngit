from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        error_messages = {
            'thumbnail':{
                'invalid':'请上传正确格式文件'
            }
        }
