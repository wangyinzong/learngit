from django.db import models
from frontus.models import FrontUser
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("Category",on_delete=models.CASCADE,null=True,related_name="articles")
    author = models.ForeignKey("frontus.FrontUser",null=True,on_delete=models.CASCADE)
    def __str__(self):
        return "<文章为:(title:%s,content:%s)>" % (self.title,self.content)
class UserExtension(models.Model):
    school = models.CharField(max_length=100)
    user = models.OneToOneField("frontus.FrontUser",on_delete=models.CASCADE,related_name='extension')
    def __str__(self):
        return "学校：%s,用户：%s" % (self.school,self.user_id)
class Tag(models.Model):
    name = models.CharField(max_length=50)
    articles = models.ManyToManyField("Article",related_name="tags")
    def __str__(self):
        return "%s:%s" % (self.articles,self.name)