from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from shortuuidfield import ShortUUIDField
from django.core import validators


class UserManager(BaseUserManager):
    def _create_user(self, telephone, username,password, **kwargs):
        if not username:
            raise ValueError('请写入用户名')
        if not telephone:
            raise ValueError('请写入电话号码')
        if not password:
            raise ValueError('请写入密码')
        user = self.model(telephone=telephone, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone, username, password, **kwargs)

    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(telephone, username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    uid = ShortUUIDField(primary_key=True)
    telephone = models.CharField(max_length=11, unique=True, validators=[validators.RegexValidator(r'1[3456789]\d{9}')])
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.__str__()


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    true_name = models.CharField(max_length=32) # 真实姓名
    pen_name = models.CharField(max_length=32)  #笔名
    image = models.ImageField(upload_to='logo')  # 作者头像
    days = models.CharField(max_length=20)   #创作天数


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32) #书名
    image = models.ImageField(upload_to='logo')#封面
    month_ticket = models.IntegerField(default=0) # 月票
    commend = models.IntegerField(default=0) # 推荐票
    category = models.CharField(max_length=30)#分类
    count = models.IntegerField()#点击量
    words = models.CharField(max_length=10)  # 字数
    content = models.TextField(max_length=200)#简介
    update_time = models.DateTimeField(auto_now=True)#更新时间
    user_book = models.ManyToManyField("User")  #用户收藏
    author = models.ForeignKey("Author", on_delete=models.CASCADE)  # 作者








