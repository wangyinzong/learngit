from django.db import models
from django.core import validators


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #thumbnail = models.FileField(upload_to='%Y/%m/%d', validators=[validators.FileExtensionValidator(['txt', 'jpg'], message="只能上传txt，jpg文件")])
    thumbnail = models.ImageField()
