from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.core import validators
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
from django.contrib.auth import get_user_model

#User.objects.all()
#Person.onjects.all() 等价的  因为person 是一个代理模型自己没什么实权 用的全是User的

# class Person(User):
#     #代理中不能有新的字段
#     #telephone = models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3456789]\d{9}')])
#     class Meta:
#         proxy = True #这里用来指定这是一个代理模型
#
#
#     @classmethod  #表示这是一个类方法
#     def get_balck_list(cli):
#         return cli.objects.filter(is_active=False)

# class UserExtension(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="extension")
#     telephone = models.CharField(max_length=11)
#     school = models.CharField(max_length=30)
#     # 当User模型有新用户进来 就需要发送信号 告诉扩展 有人来了
#
#     @receiver(post_save,sender=User)
#     def handler_user_extension(sender,instance,created,**kwargs):
#         if created:  #如果创建 走这里
#             UserExtension.objects.create(user=instance)
#         else: #更新 走这里
#             instance.extension.save()

class UserManager(BaseUserManager):
    def _create_user(self,telephone,username,email,password, **kwargs):
        if not telephone:
            raise ValueError('The given telephone must be set')
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')
        user = self.model(telephone=telephone,username=username, email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,telephone,username,password,email,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone,username=username, email=email, password=password, **kwargs)

    def create_superuser(self, telephone,username,password,email,**kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone=telephone, username=username, email=email, password=password, **kwargs)
# class User(AbstractUser):
#     telephone = models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3456789]\d{9}')],unique=True)
#     school = models.CharField(max_length=30)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'telephone' #默认django user模型采用的是 username验证 现在我们修改以后改成了 telephone
#

class User(AbstractBaseUser,PermissionsMixin):
    telephone = models.CharField(max_length=11,unique=True)
    email = models.EmailField(unique=True)
    username =  models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ('viw_article','看文章的权限'),
        ]