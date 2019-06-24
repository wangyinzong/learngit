from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.core import validators
from django.db.models.signals import post_save
from django.dispatch import receiver
# # Create your models here.
# class Person(User):
#     # 代理不能有新字段
#     class Meta:
#         proxy=True# 代理模型
#     @classmethod # 这是类方法
#     def get_black_list(cli):
#         return cli.objects.filter(is_active=True)
# class UserExtension(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="extension")
#     telephone = models.CharField(max_length=11)
#     school = models.CharField(max_length=30)
#     # 当User模型有新用户，即需要发送信号，告诉扩展新增
#     @receiver(post_save,sender=User)
#     def handler_user_extension(self,instance,created,**kwargs):
#         if created:
#             UserExtension.objects.create(user=instance)
#         else:
#             instance.extension.save()
#
#
class UserManager(BaseUserManager):
    def _create_user(self, telephone,username, email, password, **kwargs):
        if not username:
            raise ValueError('The given username must be set')
        if not telephone:
            raise ValueError('The given telephone must be set')
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(telephone=telephone,username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone,username, email, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone,username=username, email=email, password=password, **kwargs)

    def create_superuser(self,telephone, username, email, password, **kwargs):
        kwargs['is_superuser'] = True
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(telephone=telephone,username=username, email=email, password=password, **kwargs)
class User(AbstractUser):
    telephone = models.CharField(max_length=30,unique=True)
    school = models.CharField(max_length=30)

    objects = UserManager()
    # 默认django模型以username验证，修改后以telephone验证
    USERNAME_FIELD = 'telephone'